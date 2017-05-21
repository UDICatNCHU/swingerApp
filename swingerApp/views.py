# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from Swinger import Swinger
import json

def swing(request):
	if request.POST:
		s = Swinger()
		# 讀取預設模型
		s.load('LogisticRegression')
		
		post = request.POST
		post = post.dict()
		return JsonResponse({'result':s.swing(post['sentence'])}, safe=False)
	return JsonResponse({'result':'please post a sentence.'}, safe=False)

def bulk_swing(request):
	if request.POST:
		s = Swinger()
		s.load('LogisticRegression')
		post = request.POST
		post = post.dict()
		sentence = json.loads(post['sentence'])
		return JsonResponse({'result':list(map(lambda x:s.swing(x), sentence))}, safe=False)
	return JsonResponse({'result':'please post a sentence.'}, safe=False)
