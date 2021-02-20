from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

"""
功能：在页面中展示 ‘Hello World’
"""
def HelloWorld(request):
    return HttpResponse('Hello World')
