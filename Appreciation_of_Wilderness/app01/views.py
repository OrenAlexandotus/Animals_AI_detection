from django.shortcuts import render, redirect
from app01 import models
from django.contrib import messages
# Create your views here.
def init(request):

    return render(request, 'init.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    name = request.POST.get("id")
    pwd = request.POST.get("pw")
    if models.user.objects.filter(id=name).first() is None:
        return render(request, 'login.html', {"error_msg": "用户名或密码为空！请重试"})
    elif models.user.objects.filter(id=name).first().pw == pwd:
        return redirect('http://127.0.0.1:8000/init')
    return render(request, 'login.html', {"error_msg": "用户名或密码错误！请重试"})

def register(request):
    # if request.method == "GET":
    #     return render(request, 'login.html')
    name = request.POST.get("id")
    pw1 = request.POST.get("pw1")
    pw2 = request.POST.get("pw2")
    if models.user.objects.filter(id=name).first():
        return render(request, 'login.html', {"error_msg": "用户名已被注册！请重试"})
    if name == "" or pw1 == "" or pw2 == "":
        return render(request, 'login.html', {"error_msg": "用户名或密码为空！请重试"})
    if pw1==pw2:
        models.user.objects.create(id=name,pw=pw1)
        return redirect('http://127.0.0.1:8000/init')
    return render(request, 'login.html', {"error_msg": "两次密码不一致！请重试"})

def reset(request):

    return render(request, 'reset.html')

def find(request):

    return render(request, 'find.html')