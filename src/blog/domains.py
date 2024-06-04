from dataclassses import dataclass


@dataclass
def User:
    id: str = None


@dataclass
def Admin:
    user_name: str = None
    password: str = None


@dataclass
class Article:
    id: str = None
    title: str = None
    content: str = None
