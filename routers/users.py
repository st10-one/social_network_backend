from fastapi import APIRouter, Depends
from service import UserService
from schemas import UsersSchema

from dependency import usr_data_dep, file_data, priveleg_token

router = APIRouter(prefix="/social")


@router.post("/users", tags=["Users"], response_model=UsersSchema)
def add_users(user_data: usr_data_dep, Photo: file_data, user_service: UserService = Depends()):  # type: ignore
    return user_service.create_user(user_data, Photo)


@router.get("/users/{username}", tags=["Users"])
def get_one_user(username: str, user_service: UserService = Depends()):
    return user_service.get_one_user(username=username)


@router.put("/users", tags=["Users"])
def update_user_data(
    user_id: int, new_data: usr_data_dep, user_service: UserService = Depends()
):
    return user_service.update_data(user_id, new_data)


@router.delete(
    "/users/{user_id}", dependencies=[Depends(priveleg_token)], tags=["Users"]
)
def delete_user(user_id: int, user_service: UserService = Depends()):
    return user_service.delete_user(user_id)
