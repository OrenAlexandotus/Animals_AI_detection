#创建时间：2024-2-28
#创建者：李心
#修改者：
#功能：登录注册、重置密码、跳转页面、错误信息提示

from django.shortcuts import render, redirect
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
    if models.user.objects.filter(id=name).first() is None:
        return render(request, 'login.html', {"error_msg": "未注册！请重试"})
    elif models.user.objects.filter(id=name).first().pw == pwd:
        # 如果登录成功，跳转到app02的index视图
        # return redirect('http://127.0.0.1:8000/img_proc/')  # 使用app的名称和视图名称
        return redirect('/init')
    return render(request, 'login_u.html', {"error_msg": "用户名或密码错误！请重试"})

def register_u(request):
    
    '''
    功能： 用户user注册
    返回值： 注册成功跳转到app02的index视图，注册失败返回注册页面
    '''
    if request.method == "GET":
        return render(request, 'login_u.html')
    name = request.POST.get("id")
    pw1 = request.POST.get("pw1")#密码
    pw2 = request.POST.get("pw2")#密码确认
    if models.user.objects.filter(id=name).first():
        return render(request, 'login_u.html', {"error_msg": "用户名已被注册！请重试"})
    if name == "" or pw1 == "" or pw2 == "":
        return render(request, 'login_u.html', {"error_msg": "用户名或密码为空！请重试"})
    if pw1==pw2:
        models.user.objects.create(id=name,pw=pw1)
        # 如果注册成功，跳转到app02的index视图
        # return redirect('http://127.0.0.1:8000/img_proc/')  # 使用app的名称和视图名称
        return redirect('/init')
    return render(request, 'login_u.html', {"error_msg": "两次密码不一致！请重试"})

def reset(request):
    '''
    功能： 重置密码
    返回值： 重置成功跳转到app02的index视图，重置失败返回重置页面
    '''
    if request.method == "GET":
        return render(request, 'reset.html')
    name = request.POST.get("id")#id
    pwd0 = request.POST.get("pw0")#原密码
    pwd1 = request.POST.get("pw1")#新密码
    if models.user.objects.filter(id=name).first() is None:
        return render(request, 'login.html', {"error_msg": "未注册！请重试"})
    elif models.user.objects.filter(id=name).first().pw == pwd0:
        models.user.objects.filter(id=name).update(pw=pwd1)
        return redirect('init')
    return render(request, 'login.html', {"error_msg": "原密码错误！请重试"})

def login_a(request):
    if request.method == "GET":
        return render(request, 'login_a.html')
    name = request.POST.get("id")
    pwd = request.POST.get("pw")
    if models.user.objects.filter(id=name).first() is None:
        return render(request, 'login_a.html', {"error_msg": "未注册！请重试"})
    elif models.user.objects.filter(id=name).first().pw == pwd:
        return redirect('/init')
    return render(request, 'login_a.html', {"error_msg": "用户名或密码错误！请重试"})



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

def init(request):

    return render(request, 'init.html')