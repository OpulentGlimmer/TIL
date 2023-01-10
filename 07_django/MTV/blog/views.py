from django.shortcuts import render, redirect

from . models import Article

from .forms import ArticleForm
# Create your views here.


# 글 목록 화면 (Read)
def index(request):
    # 글 목록 조회
    # db article  관련된 레코드 전체를 조회
    articles = Article.objects.all()  # QuerySet(list)
    content = {
        'articles' : articles,
    }
    return render(request,  'blog/index.html', content)
# 글 상세 화면 (Read)
def detail(request, article_pk):
    # db >  articles > 특정 레코드 조회
    article = Article.objects.get(pk=article_pk)
    context = { 'article' : article, }
    return render(request, 'blog/detail.html', context)


# 글 쓰기 화면 (Create)
def new(request):
    article_form = ArticleForm()
    context = { 'article_form' : article_form,}
    # return render(request, 'blog/new.html')
    return render(request, 'blog/form_new.html', context)

# 글 DB에 실제 저장
def create(request):
    # 새로운 article 객체 생성(레코드 추가)
    # article = Article()
    article_form = ArticleForm(request.POST)
    
    # Validation (데이터 유효성 검사)
    # 넘어온 데이터가 유효하다면,
    if article_form.is_valid():
         # 저장하고,
        article = article_form.save()
        # detail 페이지로 이동

    # article.title = request.POST['title']
    # article.content = request.POST['content']
    # article.save()

    # detail 로 redirect 하자
    # return redirect('blog:detail', article.pk)
        return redirect('blog:detail', article.pk)
    # 넘어온 데이터가 유효하지 않다면
    else:
        # 다시 데이터 입력 html 출력
        context = { 'article_form' : article_form, }
        return render(request, 'blog/form_new.html', context)

# 글 수정 화면 (Update)
def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article' : article }
    return render(request, 'blog/edit.html', context)

# 글 DB에 실제 수정
def update(request, article_pk):
    # 기존의 article 객체 조회(레코드 검색)
    article = Article.objects.get(pk=article_pk)
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
     # detail 로 redirect 하자
    return redirect('blog:detail', article.pk)

# 글 삭제 ?? (Delete)
def delete(request, article_pk):
    if request.method == 'POST':
    # 특정 게시글을 지운다.
    # 1. 고른다.
        article = Article.objects.get(pk=article_pk)
    # 2. 지운다.
        article.delete()
    return redirect('blog:index')