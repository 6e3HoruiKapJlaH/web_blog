from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

from .models import Article


def index(request):
    articles_list = Article.objects.order_by('-title')[:3]
    return(render(request, 'index.html', {'articles_list' : articles_list}))


def contacts(request):
     return(render(request, 'contacts.html'))

def detail(request, article_id):
    pass