from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	data = {'title':'Articles'}
	return render(request,'front/blog/index.html',data)