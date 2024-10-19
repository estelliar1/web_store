from django.shortcuts import render
from django.http import HttpResponse


def product_list(request):
    template_name = 'catalog/product_list.html'
    return render(request, template_name)


def product_detail(request):
    return HttpResponse('Какой-то товар')
