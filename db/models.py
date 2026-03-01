from dataclasses import dataclass

@dataclass
class UsersModel:
    first_name = str
    last_name = str
    username = str
    bio = str

@dataclass
class PostModel:
    user_id = int
    content = str

@dataclass
class LikesModel:
    user_id = int
    post_id = int