from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('searchengine.searchviews',
    url(r'^searchengine-form/$', 'search_form', name='search_form'),
    url(r'^searchengine/$',  'search', name= 'search'),
    url(r'page/onclick/(\w\w)/([a-zA-Z0-9_ ]*)/$', 'onclickview', name='onclickview')
    
)


urlpatterns += patterns('searchengine.searchviews',
    url(r'^list/$', 'list', name='list'),
    )

