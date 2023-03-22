# polls/urls.py
from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # polls/create
    path('create/', views.create_question, name='create_question'),
    # polls
    path('', views.question_index, name='question_index'),
    # polls/1/
    path('<int:question_pk>/', views.question_detail, name='question_detail'),
    # polls/1/update
    path('<int:question_pk>/update', views.question_update, name='question_update'),
    # polls/1/delete
    path('<int:question_pk>/delete', views.question_delete, name='question_delete'),
    
    path('<int:question_pk>/delete/<int:reply_pk>/delete_reply', views.delete_reply, name='delete_reply'),
]
