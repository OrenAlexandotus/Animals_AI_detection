#创建时间：2024-2-28
#创建者：李心
#修改者：
#功能：登录注册、重置密码、跳转页面、错误信息提示

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app01 import models
from django.contrib import messages
# Create your views here.
def index(request):

    return render(request, 'index.html')

def login_u(request):
    '''
    功能： 用户user登录
    返回值：登录成功跳转到app02的index视图，登录失败返回登录页面
    '''
    if request.method == "GET":
        return render(request, 'login_u.html')
    name = request.POST.get("id")
    pwd = request.POST.get("pw")
    user = authenticate(request, username=name, password=pwd)
    if user is not None:
        login(request,user)
        return redirect('/user_init')
    else:
        messages.error(request, "用户名或密码错误！请重试")
        return render(request, 'login_u.html')
# 注销
def logout_u(request):
    logout(request)
    return redirect('/init')

def register_u(request):
    
    '''
    功能：用户user注册
    返回值：注册成功跳转到app02的index视图，注册失败返回注册页面
    '''
    if request.method == "GET":
        return render(request, 'login_u.html')  # 注意更正为正确的模板名称
    username = request.POST.get("id")
    password1 = request.POST.get("pw1")  # 密码
    password2 = request.POST.get("pw2")  # 密码确认
    if User.objects.filter(username=username).exists():
        messages.error(request, "用户名已被注册！请重试")
        return render(request, 'login_u.html')
    if username == "" or password1 == "" or password2 == "":
        messages.error(request, "用户名或密码为空！请重试")
        return render(request, 'login_u.html')
    if password1 == password2:
        User.objects.create_user(username=username, password=password1)
        # 如果注册成功，重定向到初始化页面
        return redirect('/user_init')  # 使用name来引用URL
    else:
        messages.error(request, "两次密码不一致！请重试")
        return render(request, 'login_u.html')

def login_a(request):
    if request.method == "GET":
        return render(request, "login_a.html")
    name = request.POST.get("id")
    pwd = request.POST.get("pw")
    if models.admin.objects.filter(id=name).first() is None:
        return render(request, "login_a.html", {"error_msg": "未注册！请重试"})
    elif models.admin.objects.filter(id=name).first().pw == pwd:
        return redirect("/admin_init")
    return render(request, "login_a.html", {"error_msg": "用户名或密码错误！请重试"})

# def find(request):
#     if request.method == "GET":
#         return render(request, 'find.html')
#     name = request.POST.get("id")#id
#     pwd0 = request.POST.get("pw0")#原密码
#     pwd1 = request.POST.get("pw1")#新密码
#     if models.user.objects.filter(id=name).first() is None:
#         return render(request, 'login.html', {"error_msg": "未注册！请重试"})
#     elif models.user.objects.filter(id=name).first().pw == pwd0:
#         models.user.objects.filter(id=name).update(pw=pwd1)
#         return redirect('http://127.0.0.1:8000/init')
#     return render(request, 'login.html', {"error_msg": "原密码错误！请重试"})

def admin_init(request):

    return render(request, 'admin.html')


def user_init(request):

    return render(request, 'user.html')