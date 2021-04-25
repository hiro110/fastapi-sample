import sys, os
from enum import Enum
from typing import List, Optional

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import users, items

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(users.router)
app.include_router(items.router)
