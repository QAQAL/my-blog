import logging

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound

from .models import Article, Note


logger = logging.getLogger('django')


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


def note(request):
    if request.method == 'POST':
        body = eval(request.body)
        title = body.get('title')
        body = body.get('body')
        data = {
            'title': title,
            'body': body
        }
        Note.objects.create(**data).save()

    elif request.method == 'GET':
        data = list(Note.objects.all().values())

    else:
        return HttpResponseNotFound('notFoundError')

    return JsonResponse({'data': data}, json_dumps_params={'ensure_ascii': False})


def subject(request):
    pass


