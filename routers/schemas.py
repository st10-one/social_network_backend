from pydantic import BaseModel, Field
from typing import Annotated


ids = Annotated[int, Field(ge=0)]

class UsersSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    bio: str | None = None

    model_config = {"from_attributes": True}


class PostsSchema(BaseModel):
    user_id: ids
    content: str

    model_config = {"from_attributes": True}


class LikesSchema(BaseModel):
    user_id: ids
    post_id: ids

    model_config = {"from_attributes": True}
