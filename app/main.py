import sys, os
from enum import Enum

from fastapi import FastAPI
from typing import List, Optional
from starlette.middleware.cors import CORSMiddleware

# from db import Session
from routers import users, items
from middlewares import sample

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.add_middleware(sample.SampleMiddleware)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(users.router)
app.include_router(items.router)
