from datetime import datetime
from sqlalchemy import String,Float,Integer,DateTime,Text,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.db import Base
class Project(Base):
    __tablename__="projects"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(160))
    city:Mapped[str]=mapped_column(String(80),default="Երևան")
    building_type:Mapped[str]=mapped_column(String(50),default="residential")
    area_sqm:Mapped[float]=mapped_column(Float)
    floors:Mapped[int]=mapped_column(Integer,default=1)
    planned_days:Mapped[int]=mapped_column(Integer,default=180)
    budget_amd:Mapped[float]=mapped_column(Float)
    progress_pct:Mapped[float]=mapped_column(Float,default=0)
    created_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)
    risks:Mapped[list["Risk"]]=relationship(back_populates="project",cascade="all, delete-orphan")
class Material(Base):
    __tablename__="materials"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(120))
    category:Mapped[str]=mapped_column(String(60))
    unit:Mapped[str]=mapped_column(String(30))
    price_amd:Mapped[float]=mapped_column(Float)
    supplier:Mapped[str]=mapped_column(String(120))
    city:Mapped[str]=mapped_column(String(80),default="Երևան")
class Risk(Base):
    __tablename__="risks"
    id:Mapped[int]=mapped_column(primary_key=True)
    project_id:Mapped[int]=mapped_column(ForeignKey("projects.id"))
    category:Mapped[str]=mapped_column(String(60))
    severity:Mapped[str]=mapped_column(String(20))
    score:Mapped[float]=mapped_column(Float)
    description:Mapped[str]=mapped_column(Text)
    project:Mapped["Project"]=relationship(back_populates="risks")
