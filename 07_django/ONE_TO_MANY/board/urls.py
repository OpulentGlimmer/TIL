# # board 앱 폴더의 urls.py에 urlpatterns 리스트에 URL를 만들기 위해 path라는 함수를 가져온다.
from django.urls import path
# 현재 폴더에 있는 views.py를 사용할 수 있게 가져온다.
from . import views

app_name = 'board'

# board 앱 폴더의 urls.py에 urlpatterns 리스트에 있는 URL과 one_to_many URL이 들어올 때 어떻게 처리해야 결정해야 한다.
urlpatterns = [
    # articles/create/ (생성)
    path('create/', views.create_article, name='create_article'),

    # 목록 페이지 만들기
    # URL이 articles로 쓰일 때 views.index()함수로 가고, 그 이름은 article_index 로 하겠다.
    # articles/
    path('', views.article_index, name='article_index'),

    
    # articles/1/ (삭제)
    path('<int:article_pk>/', views.article_detail, name='article_detail'),

    # article/1/update/
    path('<int:article_pk>/update/', views.update_article, name='update_article'),
    # article/1/delete/
    path('<int:article_pk>/delete/', views.delete_article, name='delete_article'),

    # articles/1/comments/create/  (댓글 생성)
    path('<int:article_pk>/comments/create/', views.create_comment, name='create_comment'),
    # articles/1/comments/2/delete/ : 1번 article에 달려 있는 2번 comments를 지우겠다
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
]
