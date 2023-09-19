from django.http import HttpResponseNotFound
from django.shortcuts import render


def index(request, **kwargs):
    kwargs.update({'title': 'Главная'})
    return render(request, 'common/homepage.html', kwargs)


def pageNotFound(request, exception):
    return HttpResponseNotFound(content='<h1>Page Not Found</h1>')
