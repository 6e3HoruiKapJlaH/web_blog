from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import redirect

from .models import Article


def index(request):
    return (render(request, 'index.html'))


def contacts(request):
    return (render(request, 'contacts.html'))


def see_more(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статьи нет, полудурок")
    return (render(request, 'article.html'))
