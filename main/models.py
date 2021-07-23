from django.db import models

class Article(models.Model):

    title = models.CharField('Article name', max_length = 200 )
    #pub_date = 
    text = models.TextField('Article text') 
    img_url = models.URLField('picture png', max_length = 250)	


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.CharField('Author nickname', max_length = 50)
    text = models.TextField('Comment text', max_length = 350)
    avatar = models.ImageField(upload_to='images/')