from django.urls import path

from .views import ArticleViewDetail, ArticleViewList, AuthorViewList

urlpatterns = [
    path('authors', AuthorViewList.as_view()),
    path('articles', ArticleViewList.as_view()),
    path('articles/<int:pk>', ArticleViewDetail.as_view())
]
