from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import redirect

from .models import Article


def cut_to_500_symb(article_list):
    for a in article_list:
        a.text = a.text[:500] 
    return article_list    


def index(request):
    articles_list = cut_to_500_symb( Article.objects.order_by('title')[:3])
    
    articles_dict = dict([
        ('articles_list', articles_list)
        ])

    return (render(request, 'index.html', articles_dict))


def index_list(request, list_id):

    current_3_articles = Article.objects.order_by('title')[3 * (list_id - 1):3 * list_id]

    if list_id <= 0:
        raise Http404("Страницы нет, полудурок, уходи отсюда")
    elif current_3_articles.count() == 0:
        raise Http404("Страницы нет, полудурок, уходи отсюда")

    else:
        len_list = Article.objects.count() / 3

        articles_list = current_3_articles
        articles_list = cut_to_500_symb(articles_list)

        articles_dict = dict([
         ('articles_list', articles_list),
         ('list_id', list_id), 
         ('back_id', list_id - 1), 
         ('next_id', list_id + 1), 
         ('len_list', len_list)
         ])

        return (render(request, 'index.html', articles_dict))



def contacts(request):
    return (render(request, 'contacts.html'))


def see_more(request, article_id):
    try:
        current_aticle = Article.objects.get(id=article_id)
    except:
        raise Http404("Статьи нет, полудурок")
    
    articles_dict = dict([
         ('article', current_aticle)
         ])
    return (render(request, 'article.html', articles_dict))
