from fastapi import Body, Form, Depends
from fastapi import HTTPException, status

from typing import Annotated

from schemas import UsersSchema


def user_data(
    first_name: str = Form(...),
    last_name: str = Form(...),
    username: str = Form(...),
    bio: str | None = Form(None),
) -> UsersSchema:
    return UsersSchema(
        first_name=first_name, last_name=last_name, username=username, bio=bio
    )


def priveleg_token(token: str = Body(embed=True)):
    if token != "secret":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return {"success": True}


UserDep = Annotated[UsersSchema, Depends(user_data)]
