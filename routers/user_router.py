from fastapi import APIRouter

from models import User


user_router = APIRouter()


@user_router.get("/users")
def list_users():
    return {"users": ["a", "b", "c"]}


@user_router.get("/users/{user_id}")
def get_user_details(user_id: int):
    return {"user_id": user_id}


@user_router.post('/users')
def save_user(user: User):
    return {'name': user.name,
            'age': user.age}
