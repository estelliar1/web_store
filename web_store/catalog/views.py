from django.shortcuts import render
from django.http import HttpResponse

def product_list(request):
    return HttpResponse('Каталог товаров')

def product_detail(request):
    return HttpResponse('Какой-то товар')

