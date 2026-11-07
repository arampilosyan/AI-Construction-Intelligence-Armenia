from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.db import Base,engine
from app.api.routes import router
Base.metadata.create_all(bind=engine)
app=FastAPI(title="AI Construction Intelligence — Armenia",version="1.0.0")
app.include_router(router)
static=Path(__file__).parent/"static"
app.mount("/static",StaticFiles(directory=static),name="static")
@app.get("/health")
def health(): return {"status":"ok"}
@app.get("/")
def home(): return FileResponse(static/"index.html")
