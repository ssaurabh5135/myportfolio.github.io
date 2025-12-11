from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ERP System API")

app.include_router(auth_router.router)
