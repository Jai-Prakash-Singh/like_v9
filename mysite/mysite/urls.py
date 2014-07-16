from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^searchengine/admin/', include(admin.site.urls)),
    url(r'^searchengine/', include('searchengine.urls')),
    url(r'^searchengine/books/', include('books.urls')),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.conf.urls.defaults import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead


urlpatterns += patterns('',
    url(r'^searchengine/hello/$', cache_page(hello, 60 * 15)),
    url(r'^searchengine/time/$', cache_page(current_datetime, 60 * 15)),
    url(r'^searchengine/time/plus/(\d{1,2})/$', cache_page(hours_ahead, 60 * 15)),
)



urlpatterns += patterns('',
    # ... the rest of your URLconf goes here ...
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
