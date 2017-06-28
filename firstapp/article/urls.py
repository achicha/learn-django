from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^1/', 'article.views.basic_one'),
    url(r'^2/', 'article.views.template_two'),
    url(r'^3/', 'article.views.template_three_simple'),

)
