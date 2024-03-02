import base64
import datetime
import random
import time

from django.shortcuts import render, redirect
from .forms import ImageForm
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')

def img_proc(request):
    if request.method == 'POST':
        # 前端获取的图片
        upload_img = request.FILES.get('img')
        # 构造文件名和文件路径
        upload_img.name = 'photo_' + str(int(time.time())) + '.' + upload_img.name.split('.')[-1]
        if upload_img.name.split('.')[-1] not in ['jpeg', 'jpg', 'png']:
            return HttpResponse('<h1 style="color:red;">输入文件有误</h1>')
        # 基础路径
        base_url = u"C:/Users/wangderen4/Desktop/faceRec/static/media/"
        # 对上传的图片进行命名
        img_name = 'photo_' + str(int(time.time())) + '.jpg'
        print('当前name是:  ', img_name)
        upload_url = base_url + 'user_photo/' + img_name
        print('当前url是:  ', upload_url)
        with open(upload_url, 'wb') as f:
            # pic.chunks()循环读取图片内容，每次只从本地磁盘读取一部分图片内容，
            # 加载到内存中，并将这一部分内容写入到目录下，
            # 写完以后，内存清空；下一次再从本地磁盘读取一部分数据放入内存。
            # 就是为了节省内存空间。
            for data in upload_img.chunks():
                f.write(data)