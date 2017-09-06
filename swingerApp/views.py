# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from Swinger import Swinger
from djangoApiDec.djangoApiDec import queryString_required
import json

@queryString_required(['sentence'])
def swing(request):
	s = Swinger()
	# 讀取預設模型
	s.load('LogisticRegression')
	sentence = request.GET['sentence']
	return JsonResponse({'result':s.swing(sentence)}, safe=False)

def bulk_swing(request):
	if request.POST:
		s = Swinger()
		s.load('LogisticRegression')
		post = request.POST
		post = post.dict()
		sentence = json.loads(post['sentence'])
		return JsonResponse({'result':list(map(lambda x:s.swing(x), sentence))}, safe=False)
	return JsonResponse({'result':'please post a sentence.'}, safe=False)
