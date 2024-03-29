from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

def index_view (request):
    return HttpResponse('home_view')

def contact_view (request):
    return HttpResponse('contact_view')

def about_view (request):
    return HttpResponse('about_view')
