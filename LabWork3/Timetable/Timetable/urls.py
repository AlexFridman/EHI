"""Timetable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from app import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='homepage'),
    url(r'^faculties$', views.FacultyIndexView.as_view(), name='faculty_index'),
    url(r'^faculty/(?P<pk>[0-9]+)/$', views.FacultyDetailView.as_view(), name='faculty_detail'),
    url(r'^teachers$', views.TeacherIndexView.as_view(), name='teacher_index'),
    url(r'^teacher/(?P<pk>[0-9]+)/$', views.TeacherDetailView.as_view(), name='teacher_detail'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^timetable/$', views.TimetableSearchView.as_view(), name='timetable_search'),
    url(r'^timetable/(?P<group>\d+)/$', views.TimetableView.as_view(), name='timetable'),
]
