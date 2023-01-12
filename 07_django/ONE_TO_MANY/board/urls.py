from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # articles/create/ (생성)
    path('create/', views.create_article, name='create_article'),
    # articles/
    path('', views.article_index, name='article_index'),
    # articles/1/ (삭제)
    path('<int:article_pk>/', views.article_detail, name='article_detail'),
    # articles/1/comments/create/  (댓글 생성)
    path('<int:article_pk>/comments/create/', views.create_comment, name='create_comment'),
    # articles/1/comments/2/delete/ : 1번 article에 달려 있는 2번 comments를 지우겠다
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
]
