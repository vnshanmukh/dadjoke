from fastapi import FastAPI

import models,db
import routers.joke,routers.user,routers.auth
app = FastAPI()
def create_tables():
    models.Base.metadata.create_all(bind=db.engine)
create_tables()
app.include_router(routers.joke.router)
app.include_router(routers.user.router)
app.include_router(routers.auth.router)