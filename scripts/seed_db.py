from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app.db import Base,engine,SessionLocal
from app.models import Material,Project
Base.metadata.create_all(bind=engine)
db=SessionLocal()
try:
 if db.query(Material).count()==0:
  db.add_all([Material(name=n,category=c,unit=u,price_amd=p,supplier=s,city=city) for n,c,u,p,s,city in [
   ("Ամրան A500C","metal","կգ",420,"Demo Steel Armenia","Երևան"),("Բետոն B25","concrete","մ³",39000,"Demo Concrete","Երևան"),("Ցեմենտ M400","cement","50կգ պարկ",3300,"Demo Build Market","Երևան"),("Կարմիր աղյուս","masonry","հատ",145,"Demo Brick","Արմավիր"),("XPS ջերմամեկուսիչ","insulation","մ²",4200,"Demo Insulation","Երևան"),("Գիպսաստվարաթուղթ","finishing","թերթ",2800,"Demo Finish","Երևան"),("Մալուխ 3x2.5","electrical","մետր",850,"Demo Electric","Երևան")]])
 if db.query(Project).count()==0:
  db.add_all([Project(name="Երևան բնակելի համալիր (Demo)",city="Երևան",area_sqm=2400,floors=8,planned_days=360,budget_amd=820000000,progress_pct=32),Project(name="Արաբկիր գրասենյակային շենք (Demo)",city="Երևան",building_type="commercial",area_sqm=900,floors=5,planned_days=240,budget_amd=340000000,progress_pct=18)])
 db.commit()
 print("Demo seed records inserted.")
finally: db.close()
