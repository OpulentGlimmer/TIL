from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.CharField(max_length=200)
    # article_id
    # foreign key 쓰면 필드명에 _id 붙이지 않기
    # migrate 하면 알아서 뒤에 _id 붙음
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # CASCADE는 Article id가 없어지면 Comment에 있는 article이 없어진다는 뜻이다
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)