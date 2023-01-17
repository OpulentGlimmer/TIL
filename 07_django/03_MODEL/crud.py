# $ python manage.py shell

from board.models import Article

## Create (생성)
# 1.
article = Article()
article.title = '첫번째 글'
article.content = '와 내가 처음이야'
article.author = '박은영'
article.save()

# 2.
article = Article(title='2번글', content="까비", author='김재석')
article.save()

# 3
Article.objects.create(title='3번글', content="까까비", author='윤지원')

# ctrl + d

## Read / Retrieve (조회)
# 단일 조회
article = Article.objects.get(id=1)  # article = Article.objects.get(pk=1)해도 같다.
article.id  # article.pk해도 같다.
article.title
article.content
article.author

# 전체 조회
articles = Article.objects.all()
for article in articles:
    print(article.title)

# Update (수정)
article = Article.objects.get(id=3)  # 먼저 수정할 게시글을 고르고,
article.title = '수정한 글'
article.content = '수정합니다.'
article.save()

# Delete / Destroy(삭제)
article = Article.objects.get(id=2)
article.delete()