from fastapi import FastAPI
from . import models
from .database import engine
from .routers import products, users

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)

models.Base.metadata.create_all(engine)