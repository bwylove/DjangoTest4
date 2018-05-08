# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import *
# Create your views here.
def index(request):
    # hero=HeroInfo.objects.get(pk=1)
    # context ={'hero':hero}
    list=HeroInfo.objects.filter(isDetele=False)
    context={"list":list}
    return render(request,'booktest/index.html',context)


def show(request,id,id2):
    context={'id':id,'id2':id2}
    return render(request,'booktest/show.html',context)
# 用于模板的继承
def index2(request):
    return render(request,'booktest/index2.html')

def user1(request):
    context={'uname':'张三'}
    return render(request,'booktest/user1.html',context)
def user2(request):
    return render(request,'booktest/user2.html')

# 用于html的转义
def htmlTest(request):
    context={'t1':'<h1>123</h1>','t2':'<h1>456</h1>'}
    return render(request,'booktest/htmlTest.html',context)

# 用于Cross Site Request Forgery，跨站请求伪造csrf
def csrf1(request):
    return render(request,'booktest/csrf1.html')
def csrf2(request):
    uname=request.POST['uname']
    return HttpResponse(uname)



# 验证码
def verifyCode(request):
    from PIL import Image,ImageDraw,ImageFont
    import random
    # 创建背景色
    bgColor=(random.randrange(50,100),random.randrange(50,100),0)
    # 规定宽高
    width=100
    height=25
    # 创建画布
    image=Image.new('RGB',(width,height),bgColor)
    # 构造字体对象
    font=ImageFont.truetype('COOPBL.TTF',24)
    # 创建画笔
    draw=ImageDraw.Draw(image)
    # 创建文本内容
    text='0123ABCD'
    # 逐个绘制字符
    textTemp=''
    for i in range(4):
        textTemp1=text[random.randrange(0,len(text))]
        textTemp+=textTemp1
        draw.text((i*25,0),
                  textTemp1,
                  (255,255,255),
                font)
    # draw.text((0,0),text,(255,255,255),font)
    request.session['code']=textTemp
    # 保存到内存中
    import cStringIO
    buf=cStringIO.StringIO()
    image.save(buf,'png')
    # 将内存中的输出到客户端
    return HttpResponse(buf.getvalue(),'image/png')

def verifyTest1(request):
    return render(request,'booktest/verifyTest1.html')


def verifyTest2(request):
    code1=request.POST['code1']
    code2=request.session['code']
    if code1==code2:
        return HttpResponse('OK')
    else:
        return HttpResponse('NO')