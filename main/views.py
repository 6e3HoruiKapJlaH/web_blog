from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import redirect

from .models import Article


def index(request):
    articles_list = Article.objects.order_by('-title')[:3]
    return (render(request, 'index.html', {'articles_list': articles_list}))


def index_list(request, list_id):
    len_list = Article.objects.count()/3
    articles_list = Article.objects.order_by('-title')[3 * list_id:3 * (list_id + 1)]
    return (render(request, 'index.html', {'articles_list': articles_list, 'list_id': list_id, 'back_id': list_id - 1,
                                           'next_id': list_id + 1, 'len_list': len_list}))


def contacts(request):
    return (render(request, 'contacts.html'))


def see_more(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статьи нет, полудурок")
    return (render(request, 'article.html', {'article': a}))
