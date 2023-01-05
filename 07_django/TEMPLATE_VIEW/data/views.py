from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'data/index.html')

def hello(request, name):
    context = {
        'name':name,
    }
    return render(request, 'data/hello.html', context)

def user_input(request):
    return render(request, 'data/user_input.html')

def user_output(requset):
    # request안에서 섭씨데이터 꺼내기
    c = int(requset.POST['cel'])
    f = c * 1.8 + 32

    context = {
        'f': f,
        'username' : requset.POST['username'],
        'password' : requset.POST['password'],
    }
    return render(requset, 'data/user_output.html', context)