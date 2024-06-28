import shelve
from abc import ABC, abstractmethod

from blog.domains import Admin, Article, User


class UsersRepository(ABC):

    @abstractmethod
    def get_users(self, user_name: str | None = None, password: str | None = None) -> list[User]:
        pass


class MemoryUsersRepository(UsersRepository):

    def __init__(self):
        self.users = [
            Admin(
                id="asdf222",
                user_name="admin",
                password="ASD123",
            )
        ]

    def get_users(self, user_name: str | None = None, password: str | None = None) -> list[User]:
        filtered_users = []
        for user in self.users:
            if user_name is not None and user.user_name != user_name:
                continue
            if password is not None and user.password != password:
                continue
            filtered_users.append(user)
        return filtered_users


class ArticlesRepository(ABC):

    @abstractmethod
    def get_articles(self) -> list[Article]:
        pass

    @abstractmethod
    def create_article(self, article: Article):
        pass


class ShelveArticlesRepository(ArticlesRepository):
    def __init__(self):
        self.db_name = "articles"

    def get_articles(self) -> list[Article]:
        with shelve.open(self.db_name) as db:
            return list(db.values())

    def create_article(self, article: Article):
        with shelve.open(self.db_name) as db:
            db[article.id] = article
