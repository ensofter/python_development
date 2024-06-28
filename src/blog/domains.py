from dataclasses import dataclass


@dataclass
class User:
    id: str = None


@dataclass
class Admin(User):
    user_name: str = None
    password: str = None


@dataclass
class Article:
    id: str = None
    title: str = None
    content: str = None
