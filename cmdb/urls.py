#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from rest_framework .urlpatterns import format_suffix_patterns
from rest_framework import routers
from cmdb import views
router = routers.DefaultRouter()
router.register('hosts', views.HostViewSet)
router.register('groups', views.GroupViewSet)


urlpatterns = patterns('',
    url(r'', include(router.urls))
    # url(r'^hosts/$', views.HostListView.as_view()),
    # url(r'^host/(?P<pk>[0-9]+)/$', views.HostDetailView.as_view()),
    # url(r'^groups/$', views.GroupListView.as_view()),
    # url(r'^group/(?P<pk>[0-9]+)/$', views.GroupDetailView.as_view()),
)

# urlpatterns = format_suffix_patterns(urlpatterns)
