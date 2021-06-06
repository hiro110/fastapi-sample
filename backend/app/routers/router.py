from fastapi import APIRouter

from . import users, index

router = APIRouter()
# router.include_router(index.router, tags=["login"])
# router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(index.router)
router.include_router(users.router)