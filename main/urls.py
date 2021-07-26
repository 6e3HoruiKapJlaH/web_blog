from django.urls import path
from . import views
from django.conf import settings


#Урлы, которые обслуживает сервер
urlpatterns = [
    path('', views.index),

    path('contacts', views.contacts),

    path('<int:article_id>/', views.see_more, name='see_more'),

    path('articles_list/<int:list_id>/', views.index_list, name='index_list'),

    path('<int:article_id>/leave_comment', views.leave_comment, name='leave_comment'),

]
