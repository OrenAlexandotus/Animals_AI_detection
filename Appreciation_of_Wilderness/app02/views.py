import base64
import datetime
import random
import time
import requests

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def proc(path):
    '''
    动物识别
    '''
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
    # 二进制方式打开图片所属的[本地文件]
    f = open(path, 'rb')
    img = base64.b64encode(f.read())
    #params = {"image":img}
    params = {
        "image": img,
        "top_num": 1,      # 返回预测得分top结果数设置为5
        "baike_num": 4     # 返回百科信息数量设置为5
    }
    access_token = '[24.6c21532002858e202d2f3fd3a495c4de.2592000.1711961933.282335-54400539]'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        response_json = response.json()
        if 'result' in response_json:
            for result in response_json['result']:
                name = result['name']  # 动物名称
                score = str(round(float(result['score']) * 100, 2)) + '%'  # 置信度转换为百分比
                baike_info = result.get('baike_info', {})  # 百科信息
                baike_url = baike_info.get('baike_url', 'No baike URL')  # 百科页面链接
                description = baike_info.get('description', 'No description')  # 百科描述
                print(f"动物名: {name}, 相似度: {score}, 动物简介: {baike_url}, Description: {description}")
        else:
            print("No result in response.")
    else:
        print("Request failed.")
    return response

def index(request):
    return render(request, "./upload_image.html")

def img_proc(request):
    print(request.POST)
    print(request.FILES)
    if request.method == 'POST':
        # 前端获取的图片
        upload_img = request.FILES.get('img')
        # 构造文件名和文件路径
        upload_img.name = 'photo_' + str(int(time.time())) + '.' + upload_img.name.split('.')[-1]
        if upload_img.name.split('.')[-1] not in ['jpeg', 'jpg', 'png']:
            return HttpResponse('<h1 style="color:red;">输入文件有误</h1>')
        # 基础路径
        base_url = u"static/media/"
        # 对上传的图片进行命名
        img_name = 'photo_' + str(int(time.time())) + '.jpg'
        print('当前name是:  ', img_name)
        upload_url = base_url + u"user_photo/" + img_name
        print('当前url是:  ', upload_url)
        with open(upload_url, 'wb') as f:
            # pic.chunks()循环读取图片内容，每次只从本地磁盘读取一部分图片内容，
            # 加载到内存中，并将这一部分内容写入到目录下，
            # 写完以后，内存清空；下一次再从本地磁盘读取一部分数据放入内存。
            # 就是为了节省内存空间。
            for data in upload_img.chunks():
                f.write(data)
        result = proc(upload_url)
        
    return render(request, 'upload_image.html', {'data': result.json().result})