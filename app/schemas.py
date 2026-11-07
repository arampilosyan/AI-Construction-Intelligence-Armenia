from pydantic import BaseModel,Field,ConfigDict
from datetime import datetime
class ProjectCreate(BaseModel):
    name:str=Field(min_length=2,max_length=160)
    city:str="Երևան"
    building_type:str="residential"
    area_sqm:float=Field(gt=0)
    floors:int=Field(default=1,ge=1)
    planned_days:int=Field(default=180,ge=1)
    budget_amd:float=Field(gt=0)
    progress_pct:float=Field(default=0,ge=0,le=100)
class ProjectOut(ProjectCreate):
    id:int
    created_at:datetime
    model_config=ConfigDict(from_attributes=True)
class Estimate(BaseModel):
    area_sqm:float=Field(gt=0)
    floors:int=Field(default=1,ge=1)
    building_type:str="residential"
    finish_level:str="standard"
    contingency_pct:float=Field(default=10,ge=0,le=50)
