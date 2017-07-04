from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = "article"

    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)


class Comments(models.Model):
    class Meta:
        db_table = "comments"

    comments_date = models.DateTimeField()
    comments_text = models.TextField(verbose_name="add new comment:")
    # one-to-many relationships: 1 article -> 10 comments
    comments_article = models.ForeignKey(Article)
    comments_from = models.ForeignKey(User)
