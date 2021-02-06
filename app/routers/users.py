from typing import List, Optional

from fastapi import APIRouter, Depends

from db import session
import models, schemas, middlewares

router = APIRouter()

@router.get("/users")
@middlewares.preprocessing.sample_decorator()
def read_users():
    users = session.query(models.User).all()
    return users

@router.post("/user")
async def create_user(name: str, age: int):
    user = models.User()
    user.name = name
    user.age = age
    session.add(user)
    session.commit()

@router.put("/users")
async def update_users(users: List[schemas.User]):
    for new_user in users:
        user = session.query(models.User).\
            filter(models.User.id == new_user.id).first()
        user.name = new_user.name
        user.age = new_user.age
        session.commit()

@router.get("/users/{user_id}")
def read_user(user_id: int):
    user = session.query(models.User).\
        filter(models.User.id == user_id).first()
    return user

@router.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
