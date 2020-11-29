import sys, os
from fastapi import FastAPI
from typing import List, Optional
from starlette.middleware.cors import CORSMiddleware
from db import session
from enum import Enum
from routers import users, items
from middlewares import sample

app = FastAPI()

# ----------Middlewareの定義------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(sample.SampleMiddleware)

# ----------APIの定義------------
@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(users.router)
app.include_router(items.router)
