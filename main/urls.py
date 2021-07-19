from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contacts.html', views.contacts, name='contacts'), 

    path('<int:article_id>/', views.detail, name = 'detail'), 
]