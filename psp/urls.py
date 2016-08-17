"""psp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin
from artykul.models import Kategoria, Artykul
from django.conf.urls.static import static
from artykul import views
from django.core.urlresolvers import reverse
#from psp.artykul.models import views
urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.kategoria, name='kategoria'),
    # url(r'^$', views.lista, name='lista'),
    url(r'^kategoria/(?P<pk>\d+)/$', views.category, name='kategori'),
    url(r'^artykul/(?P<pk>\d+)/$', views.artykul, name='artykul'),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^home/$', views.home, name='home'),
    url(r'', include('artykul.urele')),
    # url(r'^photologue/', include('photologue.urls')),

#    url(r'^demo/', include('jsdemo.urls')),
]

# urlpatterns+=patterns('',
#     url(r'^photologue/', include('photologue.urls')),
#     )
urlpatterns += patterns('',
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
)
#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


def javascript_settings():
    js_conf = {
	'page_title': 'Home',
    }
    return js_conf;
