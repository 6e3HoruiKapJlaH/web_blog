from django.contrib import admin

from .models import Article, Comment

#Отображение в админке статей и комментариев
admin.site.register(Article)
admin.site.register(Comment)