from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey
import datetime
from dependency import intpk


class Base(DeclarativeBase):
    pass

class UserModel(Base):
    __tablename__ = "Users"

    id:Mapped[intpk]
    first_name:Mapped[str]
    last_name:Mapped[str]
    username:Mapped[str] = mapped_column(unique=True)
    bio:Mapped[str]
    create_at:Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow())
    update_at:Mapped[float] = mapped_column(default=datetime.datetime.utcnow, onupdate=datetime.datetime.now)


class PostModel(Base):
    __tablename__ = "Posts"

    id:Mapped[intpk]
    user_id:Mapped[int] = mapped_column(ForeignKey("Users.id", ondelete="CASCADE"))
    content:Mapped[str] 
