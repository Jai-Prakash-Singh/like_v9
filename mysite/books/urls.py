from django.conf.urls import patterns, include, url


urlpatterns = patterns('books.views',
    url(r'^search-form/$', 'search_form'),
    url(r'^search/$', 'search'),
    url(r'^contact/$', 'contact'),
    url(r'^contact/thanks/$', 'thanks'),
)
