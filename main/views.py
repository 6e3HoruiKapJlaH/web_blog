from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

from .models import Article, Comment
from .forms import CommentForm


def check_article(article_id):
    try:
        current_aticle = Article.objects.get(id=article_id)

        return current_aticle
    except:
        raise Http404("Статьи нет, полудурок")
    

def cut_to_500_symb(article_list):
    for a in article_list:
        a.text = a.text[:500] 
    return article_list    


def leave_comment(request, article_id):
    context = {}

    '''try:
        current_aticle = Article.objects.get(id=article_id)

    except:
        raise Http404("Статьи нет, полудурок")'''


    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data.get("nickname")
            text = form.cleaned_data.get("text")
            img = form.cleaned_data.get("avatar")
            obj = Comment.objects.create(
                                 username = name,
                                 text = text,
                                 avatar = img
                                 )
            obj.save()
            print(obj)
            see_more(request, article_id)

        #username = request.POST['username']
        #img = request.POST['avatar']
        #text = request.POST['comment_text']
        #obj = Comment.objects.create(
                                 #text = text,
                                 #username = username,
                                 #avatar = img
                                 #)
        #obj.save()

    else:
        form = CommentForm()
    context['form']= form

    return render(request, "article.html", context)

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


    current_aticle = check_article(article_id)
    comments_to_this_article = current_aticle.comment_set.order_by('id')

    articles_dict = dict([
         ('article', current_aticle),
         ('form', CommentForm()),
         ('comments', comments_to_this_article)
         ])
    return (render(request, 'article.html', articles_dict))
