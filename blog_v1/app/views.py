import logging

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound

from .models import Article


logger = logging.getLogger('django')


def index(request):
    return render(request, 'base.html')


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


