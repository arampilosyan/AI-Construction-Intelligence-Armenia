from fastapi.testclient import TestClient
from app.main import app
from app.db import Base,engine
import pytest
@pytest.fixture()
def client():
 Base.metadata.drop_all(bind=engine);Base.metadata.create_all(bind=engine)
 with TestClient(app) as c: yield c
 Base.metadata.drop_all(bind=engine)
def test_health(client): assert client.get("/health").json()["status"]=="ok"
def test_estimate(client):
 r=client.post("/api/estimates",json={"area_sqm":100,"floors":2})
 assert r.status_code==200 and r.json()["estimated_total_amd"]>0
def test_project_and_prediction(client):
 p=client.post("/api/projects",json={"name":"Test build","area_sqm":500,"budget_amd":100000000})
 assert p.status_code==201
 r=client.post(f"/api/projects/{p.json()['id']}/delay-prediction",json={"schedule_slippage":.6,"budget_overrun":.5,"material_shortage":.4,"weather_disruption":.3})
 assert r.status_code==200 and 0<=r.json()["delay_probability"]<=1
def test_materials(client): assert client.get("/api/materials").status_code==200
