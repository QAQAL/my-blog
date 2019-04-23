import logging, copy

from haystack.query import SearchQuerySet
from jieba import cut_for_search
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


def add_p(item, q_str_list):
    query = copy.copy(item)
    for q_str in q_str_list:
        query = query.replace(q_str, '<p>{}</p>'.format(q_str))
    return query


def search(request):
    request.encoding = 'utf8'
    q = request.GET.get('q')
    q_str_list = list(cut_for_search(q))
    print(q_str_list)
    query_set = SearchQuerySet().filter(content=q).models(Article)
    result = []
    for query in query_set:
        i = {}
        i['title'] = add_p(query.title, q_str_list)
        i['article_id'] = query.article_id
        i['content'] = add_p(query.content, q_str_list)
        result.append(i)

    return JsonResponse({'data': result})
