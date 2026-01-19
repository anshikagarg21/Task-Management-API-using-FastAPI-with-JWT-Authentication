from fastapi import FastAPI
from database import Base, engine
from routes import auth_routes, task_routes, admin_routes
 
Base.metadata.create_all(bind=engine)
 
app = FastAPI(title="Task Management API")
 
app.include_router(auth_routes.router)
app.include_router(task_routes.router)
app.include_router(admin_routes.router)