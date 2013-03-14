# -*- coding: utf-8 -*-

"""
feedjack
Gustavo Picón
urls.py
"""

from django.conf.urls.defaults import patterns

from feedjack import views



urlpatterns = patterns('',
    (r'^rss20.xml$', views.rssfeed),
    (r'^feed/$', views.atomfeed),

    (r'^feed/rss/$', views.rssfeed),
    (r'^feed/atom/$', views.atomfeed),

    (r'^feed/user/(?P<user>\d+)/tag/(?P<tag>.*)/$',  views.atomfeed),

    (r'^feed/user/(?P<user>\d+)/$', views.atomfeed),

    (r'^feed/tag/(?P<tag>.*)/$',  views.atomfeed),

    (r'^feed/atom/user/(?P<user>\d+)/tag/(?P<tag>.*)/$',views.atomfeed),
    (r'^feed/atom/user/(?P<user>\d+)/$', views.atomfeed),
    (r'^feed/atom/tag/(?P<tag>.*)/$', views.atomfeed),
    (r'^feed/rss/user/(?P<user>\d+)/tag/(?P<tag>.*)/$', views.rssfeed),
    (r'^feed/rss/user/(?P<user>\d+)/$', views.rssfeed),
    (r'^feed/rss/tag/(?P<tag>.*)/$', views.rssfeed),

    (r'^user/(?P<user>\d+)/tag/(?P<tag>.*)/$', views.mainview),
    (r'^user/(?P<user>\d+)/$', views.mainview),
    (r'^tag/(?P<tag>.*)/$', views.mainview),

    (r'^opml/$', views.opml),
    (r'^foaf/$', views.foaf),
    (r'^$', views.mainview),
)


