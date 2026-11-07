from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Project,Material,Risk
from app.schemas import ProjectCreate,ProjectOut,Estimate
from app.services.analytics import estimate,optimize
from app.services.ml import delay_prediction,risk_rules
router=APIRouter(prefix="/api")
@router.get("/dashboard/summary")
def summary(db:Session=Depends(get_db)):
    ps=db.query(Project).all()
    return {"projects_count":len(ps),"materials_count":db.query(Material).count(),"total_budget_amd":sum(p.budget_amd for p in ps),"average_progress_pct":round(sum(p.progress_pct for p in ps)/len(ps),1) if ps else 0,"currency":"AMD"}
@router.get("/materials")
def materials(q:str|None=None,db:Session=Depends(get_db)):
    query=db.query(Material)
    if q: query=query.filter(Material.name.ilike(f"%{q}%"))
    return query.order_by(Material.name).all()
@router.post("/estimates")
def estimates(x:Estimate): return estimate(x)
@router.post("/projects",response_model=ProjectOut,status_code=201)
def create_project(x:ProjectCreate,db:Session=Depends(get_db)):
    p=Project(**x.model_dump());db.add(p);db.commit();db.refresh(p);return p
@router.get("/projects",response_model=list[ProjectOut])
def projects(db:Session=Depends(get_db)): return db.query(Project).order_by(Project.created_at.desc()).all()
@router.get("/projects/{pid}",response_model=ProjectOut)
def project(pid:int,db:Session=Depends(get_db)):
    p=db.get(Project,pid)
    if not p: raise HTTPException(404,"Project not found")
    return p
@router.post("/projects/{pid}/risk-analysis")
def risk(pid:int,db:Session=Depends(get_db)):
    p=db.get(Project,pid)
    if not p: raise HTTPException(404,"Project not found")
    risks=risk_rules(p)
    for r in risks: db.add(Risk(project_id=pid,**r))
    db.commit()
    return {"project_id":pid,"risks":risks}
@router.post("/projects/{pid}/delay-prediction")
def predict(pid:int,data:dict,db:Session=Depends(get_db)):
    if not db.get(Project,pid): raise HTTPException(404,"Project not found")
    keys=["schedule_slippage","budget_overrun","material_shortage","weather_disruption"]
    try: vals=[float(data[k]) for k in keys]
    except (KeyError,TypeError,ValueError): raise HTTPException(422,"Provide four numeric risk factors between 0 and 1")
    if any(v<0 or v>1 for v in vals): raise HTTPException(422,"Risk factors must be between 0 and 1")
    return delay_prediction(*vals)
@router.post("/projects/{pid}/optimization")
def optimization(pid:int,db:Session=Depends(get_db)):
    p=db.get(Project,pid)
    if not p: raise HTTPException(404,"Project not found")
    cost=estimate(Estimate(area_sqm=p.area_sqm,floors=p.floors,building_type=p.building_type))["estimated_total_amd"]
    return optimize(p.budget_amd,cost)
