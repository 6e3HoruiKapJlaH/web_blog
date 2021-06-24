from django.db import models

class Article(models.Model):
    title = models.CharField('Article name', max_length = 200 )
    text = models.TextField('Article text') 
    img_url = models.URLField('picture png', max_length = 250)	

