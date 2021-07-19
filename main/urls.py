from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path('contacts', views.contacts), 



    path('<int:article_id>/', views.see_more, name = 'see_more'),
]