from django.contrib import admin
from models import Article, Comments


# Register your models here.
class ArticleInline(admin.StackedInline):
    """
    add comments field to Admin page
    """
    model = Comments
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    """
    This is settings for Article
    """
    fields = ['article_title', 'article_text', 'article_date']  # only these fields will be shown in admin page
    inlines = [ArticleInline]                                   # constrains that shows Articles
    list_filter = ['article_date']                              # filter out Articles in Admin page by date

admin.site.register(Article, ArticleAdmin)  # register Article for Admin app
