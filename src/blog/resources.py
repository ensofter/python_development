from fastapi import APIRouter, status, HTTPException

from blog.domains import Admin
from blog.schemas import (
    GetArticlesModel, CreateArticleModel, LoginModel, GetArticleModel, ErrorModel
)
from blog import services
from blog.repositories import ShelceArticlesRepository, MemoryUsersRepository


router = APIRouter()


@router.get("/articles", response_model=GetArticlesModel)
def get_articles() -> GetArticlesModel:
    articles = services.get_articles(articles_repository=ShelveArticlesRepository())
    return GetArticlesModel(
    items=[
        GetArticleModel(id=article.id, title=article.title, content=article.content)
        for article in articles
    ])


@router.post("/articles", response_model=GetArticleModel, status_code=status.HTTP_201_CREATED, response={201:{"model": GetArticleModel}, 401:{"model": ErrorModel}, 403: {"model": ErrorModel}})
def create_article(article: CreateArticleModel, credentials: LoginModel):
    current_user = services.login(
        user_name=credentials.user_name,
        password=credentials.password,
        users_repository=MemoryUsersRepository()
    )
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNATHORIZED, detail='Unauthorized user'
        )
    if not isinstance(current_user, Admin):
        raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden resource"
        )

    article = services.create_article(
        title=article.title,
        content=article.content,
        articles_repository=ShelveArticlesRepository(),
    )

    return GetArticleModel(id=article.id, title=article.title, content=article.content)

