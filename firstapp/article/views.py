from django.shortcuts import render_to_response, redirect
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context                     # store variables before send them to template

from forms import CommentForm
from models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist   # if we do not have data in our DB
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib import auth


# Create your views here.
def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is %s view</body></html>" % view
    return HttpResponse(html)


def template_two(request):
    view = "template_two"
    t = get_template('my_view.html')
    html = t.render(Context({'name': view}))  # add variable to our template via Context()
    return HttpResponse(html)


def template_three_simple(request):
    view = "template_three"
    return render_to_response('my_view.html', {'name': view})


def articles(request, page_number=1):
    """blog wall with all articles"""
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 3)   # Paginator_object() shows 3 articles per page
    return render_to_response('articles.html', {'articles': current_page.page(page_number),
                                                'username': auth.get_user(request).username})


def article(request, article_id=1, page_number=1):
    """full content of single article"""
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)                        # get only 1 result
    all_comments = Comments.objects.filter(comments_article_id=article_id)  # filter possible many results
    current_comment_page = Paginator(all_comments, 3)
    args['comments'] = current_comment_page.page(page_number)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)


def addlike(request, article_id):
    """add likes to article"""
    path = request.META.get('HTTP_REFERER')             # remember Referrer page
    try:
        if article_id in request.COOKIES:
            return redirect(path)
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect(path)                   # cookies stores in response
            response.set_cookie(article_id, "test")     # save {1:'test'} in our cookie file
            return response
    except ObjectDoesNotExist:
        raise Http404


def addcomment(request, article_id):
    if request.POST and 'pause' not in request.session:
        form = CommentForm(request.POST)        # only post requests possible
        if form.is_valid():                     # form validation
            comment = form.save(commit=False)   # not save comment automatically
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()                         # save in DB
            request.session.set_expiry(60)      # create session object, which will be expired in 60 second.
            request.session['pause'] = True     # add {'pause': True} to session
    return article(request, article_id)
