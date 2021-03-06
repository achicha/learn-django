from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^1/', 'article.views.basic_one'),
    url(r'^2/', 'article.views.template_two'),
    url(r'^3/', 'article.views.template_three_simple'),
    url(r'^articles/all/$', 'article.views.articles'),                     # get all articles

    # (?<>) this variable we will use in template
    url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^articles/get/(?P<article_id>\d+)/page/(?P<page_number>\d+)/$', 'article.views.article'),
    url(r'^articles/addlike/(?P<article_id>\d+)/$', 'article.views.addlike'),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
    url(r'^page/(\d+)/$', 'article.views.articles'),
    #url(r'^comments/(\d+)/$', 'article.views.article')
    url(r'^', 'article.views.articles'),
)
