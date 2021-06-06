from sqlalchemy.orm import Session

import models, schemas, middlewares

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.UserSchema):
    user = models.User()
    user.name = name
    user.age = age
    db.add(user)
    db.commit()
    db.refresh(user)
    return user