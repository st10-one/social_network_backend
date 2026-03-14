from abc import ABC, abstractmethod


class AbstractUserRepository(ABC):
    @abstractmethod
    def add_user():
        raise NotImplemented

    @abstractmethod
    def get_user_name():
        raise NotImplemented

    @abstractmethod
    def update_user():
        raise NotImplemented

    def delete_user():
        raise NotImplemented


class AbstractPostRepository(ABC):
    @abstractmethod
    def add_posts():
        raise NotImplemented

    @abstractmethod
    def delete_post():
        raise NotImplemented



class AbstractLikeRepository(ABC):
    @abstractmethod
    def add_like():
        raise NotImplemented

    @abstractmethod
    def delete_like():
        raise NotImplemented
