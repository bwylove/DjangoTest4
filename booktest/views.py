# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
# Create your views here.
def index(request):
    # hero=HeroInfo.objects.get(pk=1)
    # context ={'hero':hero}
    list=HeroInfo.objects.filter(isDetele=False)
    context={"list":list}
    return render(request,'booktest/index.html',context)
