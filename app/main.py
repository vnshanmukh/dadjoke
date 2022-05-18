from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models,db
import routers.joke,routers.user,routers.auth
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def create_tables():
    models.Base.metadata.create_all(bind=db.engine)
create_tables()
app.include_router(routers.joke.router)
app.include_router(routers.user.router)
app.include_router(routers.auth.router)