from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import redirect

from .models import Article


def index(request):
    articles_list = Article.objects.order_by('-title')[:3]
    return(render(request, 'index.html', {'articles_list' : articles_list}))


def contacts(request):
    return (render(request, 'contacts.html'))


def see_more(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статьи нет, полудурок")
    return (render(request, 'article.html', {'article' : a}))


