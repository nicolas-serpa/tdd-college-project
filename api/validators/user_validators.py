from pydantic import BaseModel, EmailStr
from api.validators.post_validators import Post


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: str
    posts: list[Post] = []
    is_active: bool = True
    is_admin: bool = False

    class Config:
        from_attributes = True
