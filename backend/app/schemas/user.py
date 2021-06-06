from typing import Optional

from pydantic import BaseModel

class UserSchema(BaseModel):
    email: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None

class UserCreateSchema(UserSchema):
    email: str
    password: str

class UserInDB(UserSchema):
    password: str