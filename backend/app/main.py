import sys, os
from enum import Enum
from typing import List, Optional

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router.router)