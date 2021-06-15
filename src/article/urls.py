from django.urls import path

from .views import ArticleViewDetail, ArticleViewList

urlpatterns = [
    path('articles', ArticleViewList.as_view()),
    path('articles/<int:pk>', ArticleViewDetail.as_view())
]
