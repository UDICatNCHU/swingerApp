# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from Swinger import Swinger
# Create your views here.
s = Swinger()
# 讀取方式2選1
s.load('NuSVC') # 讀取預設模型

def swing(request):
	if request.POST:
		post = request.POST
		post = post.dict()
		return JsonResponse({'result':s.swing(post['sentence'])}, safe=False)
	return JsonResponse({'result':'please post a sentence.'}, safe=False)
