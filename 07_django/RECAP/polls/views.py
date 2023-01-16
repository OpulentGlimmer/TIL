from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_http_methods ,require_safe, require_POST
from django.contrib.auth.decorators import login_required
from .models import Question, Reply
from .forms import QuestionForm, ReplyForm

@login_required
@require_http_methods(['GET', 'POST'])
def create_question(request):
    pass

@require_safe
def question_index(request):
    questions = Question.objects.all()
    context = { 'questions' : questions}
    return render(request, 'polls/question_index.html', context)

@require_safe
def question_detail(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    form = ReplyForm
    context = { 'question' : question, 'form' : form }
    return render(request, 'polls/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    # 요청 보낸 사용자가 질문 작성자가 아니라면,
    if request.user != question.user:
        return HttpResponseForbidden('권한이 없습니다.')
    elif request.method == 'POST':
        return redirect('polls:detail.html/', question_pk)

@login_required
@require_POST
def delete_question(request, question_pk):
    question = get_object_or_404(Question, question_pk)
    if question.user != request.user:
        return redirect('polls:index.html/', question_pk)


@login_required
@require_POST
def delete_reply(request, question_pk, reply_pk):
    question = get_object_or_404(Question, pk=question_pk)
    reply = get_object_or_404(Reply, pk=reply_pk)
    if reply.user != request.user:
        return redirect('polls:index.html/', question_pk)
  
