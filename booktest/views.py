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