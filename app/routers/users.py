from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import SessionLocal, ENGINE
import models, schemas, middlewares, crud

router = APIRouter()

def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()

@router.get("/users")
@middlewares.preprocessing.sample_decorator()
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.post("/user")
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# @router.put("/users")
# async def update_users(users: List[schemas.User]):
#     for new_user in users:
#         user = session.query(models.User).\
#             filter(models.User.id == new_user.id).first()
#         user.name = new_user.name
#         user.age = new_user.age
#         session.commit()

@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# @router.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#     user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item
