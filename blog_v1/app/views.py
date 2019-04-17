import logging

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.db.models import Q
from haystack.forms import SearchForm

from .models import Article


logger = logging.getLogger('django')



def search(request):
    #获得查询关键字
    sform = SearchForm(request.GET)
    posts = sform.search()
    return posts


def index(request):
    logger.error('hello world! ' * 10000)
    return HttpResponse('Hello World!')


def article(request):
    if request.method == 'POST':
        body = eval(request.body)
        brief = body.get('brief')
        title = body.get('title')
        content = body.get('content')
        data = {
            'brief': brief,
            'title': title,
            'content': content
        }
        Article.objects.create(**data).save()

    elif request.method == 'GET':
        data = list(Article.objects.all().values())

    else:
        return HttpResponseNotFound('notFoundError')

    return JsonResponse({'data': data})


def subject(request):
    pass


