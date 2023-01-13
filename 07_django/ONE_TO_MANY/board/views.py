from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import(require_http_methods, require_POST, require_safe)
from django.contrib.auth.decorators import login_required

from .models import Article, Comment
from .forms import ArticleForm, CommentForm

@login_required
@require_http_methods(['GET', 'POST'])
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # is_valid (form.check(), form.is_ok()하나로 합쳐짐), form.is_valid해야 form.save()가 가능하다.
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            # redirect는 브라우저 요청을 다시 요청한다. 'GET articles/1/' = 'board:article_detail'와 같다.
            return redirect('board:article_detail', article.pk)

    else:
        form = ArticleForm()
    context = { 'form' : form }
    return render(request, 'board/form.html', context)



# 목록 페이지 만들기

# 새로 만든 index()함수는 장고가 기본적으로 제공하는 render() 함수를 사용해 템플릿 폴더에서 board폴더의
# index.html파일을 찾아 방문자에게 보내준다.
# HTTP를 요청하기 위해 request함수라는 것을 쓴다.
# board에 페이지에 포스트 목록 나열할 때에는 models.py에 있는 Article에 있는 모든 레코드를 가져와서
# articles에 저장한다.
# render() 함수는 request 객체를 첫번째 인수로 받고, 
# 템플릿 이름을 두번째 인수로 받으며, 
# context 사전형 객체를 세번째 선택적(optional) 인수로 받는다.
# 따라서 content변수에 articles를 딕셔너리 형태로 추가한다.

@require_safe
def article_index(request):
    articles = Article.objects.all()
    context = {'articles':articles,}
    return render(request, 'board/index.html', context)







@require_safe  # GET, (HEAD) 요청만 허용하겠다.
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm()
    context = {'article':article, 'form' : form }
    return render(request, 'board/detail.html', context)



@login_required
@require_POST  # 댓글을 달면 db에 영향이 가서 POST이다.
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # CommentForm(request.POST)에 데이터가 Comment에 있는 content만 있고, article_id는 넘어오지 않음.
    # 따라서 forms.py에 article에 있는 것을 가져와야 한다.
    form = CommentForm(request.POST)
    # 만약에 form이 유효하다면
    if form.is_valid():
        # 완전 저장시 NOT NULL 에러 뜨니까, 직전에 멈춰 주세요.
        comment = form.save(commit=False)
        comment.user = request.user
        # 나머지 직접 할게요.
        comment.article = article
        comment.save()
    return redirect('board:article_detail', article_pk)

# comment_pk가 삭제해야 하니까 comment_pk가 있어야 한다
@login_required
@require_POST
def delete_comment(request, article_pk, comment_pk):
    # comment 객체를 잡는다
    comment = get_object_or_404(Comment, pk=comment_pk)
    # article = get_object_or_404(Article, pk=article_pk)
    # return redirect('board:article_detail', article.pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('board:article_detail', article_pk)