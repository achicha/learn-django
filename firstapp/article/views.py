from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context                 # store variables before send them to template
from article.models import Article, Comments


# Create your views here.
def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is %s view</body></html>" % view
    return HttpResponse(html)


def template_two(request):
    view = "template_two"
    t = get_template('my_view.html')
    html = t.render(Context({'name': view}))        # add variable to our template via Context()
    return HttpResponse(html)


def template_three_simple(request):
    view = "template_three"
    return render_to_response('my_view.html', {'name': view})


def articles(request):
    """blog wall with all articles"""
    return render_to_response('articles.html', {'articles': Article.objects.all()})


def article(request, article_id=1):
    """full content of single article"""
    return render_to_response('article.html', {'article': Article.objects.get(id=article_id),
                                               'comments': Comments.objects.filter(comments_article_id=article_id)})
