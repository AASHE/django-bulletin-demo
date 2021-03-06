from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoBulletinDemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/',
        include(admin.site.urls)),

    url(r'^',
        include('bulletin.urls', namespace='bulletin')),

    (r'^accounts/',
     include('registration.urls')),

    (r'^accounts/',
     include('django.contrib.auth.urls')),
)
