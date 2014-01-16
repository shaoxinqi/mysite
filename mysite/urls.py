#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from mysite import views
from views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/login/$',views.login),
    url(r'^accounts/logout/$',views.logout),
    url(r'^accounts/auth/$',views.auth_view),
    url(r'^accounts/loggedin/$',views.loggedin),
    url(r'^accounts/invalid/$',views.invalid_login),
    url(r'^accounts/register/$',views.register_user),
    url(r'^accounts/register_success/$',views.register_success),
    url(r'^accounts/add/$',views.add),
    url(r'^accounts/add_success/$',views.add_success),
    url(r'^accounts/query/$',views.query),
    url(r'^accounts/result/$',views.result),

    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
