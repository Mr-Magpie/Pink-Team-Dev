"""pinkproject URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    #Home Page (index.html)
    url(r'^$', 'news.views.index', name='index'),

    #Test Development Pages

    url(r'^admin/', include(admin.site.urls)),

    #url example  - http://127.0.0.1:8000/kang_dev2/

    url(r'^main_news/', 'news.views.main_news', name='liam_home'),
    url(r'^add_twitter', 'news.views.add_twitter', name='liam_home'),
    url(r'^your_news/', 'news.views.your_news', name='liam_home'),



    url(r'^my_profile/', 'news.views.my_profile', name='my_profile'),

    url(r'^my_profile/', 'news.views.my_profile', name='my_profile'),


    #drop down
    url(r'^preferences/', 'news.views.preferences', name='preferences'),
    url(r'^analytics/', 'news.views.analytics', name='analytics'),
    url(r'^settings/', 'news.views.settings', name='settings'),
    url(r'^options/', 'news.views.options', name='options'),
    url(r'^inbox/', 'news.views.inbox', name='inbox'),
    url(r'^account_information/', 'news.views.account_information', name='account_information'),

    #registration
    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^liam_dev/', 'liam_dev.views.liam_dev', name='liam_home'),
    url(r'^liam_dev2/', 'liam_dev.views.liam_dev2', name='liam_home'),
    url(r'^liam_dev3/', 'liam_dev.views.liam_dev3', name='liam_home'),

    url(r'^james_dev/', 'james_dev.views.james_dev', name='james_home'),
    url(r'^james_dev2/', 'james_dev.views.james_dev2', name='james_home'),
    url(r'^james_dev3/', 'james_dev.views.james_dev3', name='james_home'),


    url(r'^shuyu_dev/', 'shuyu_dev.views.shuyu_dev', name='shuyu_home'),
    url(r'^shuyu_dev2/', 'shuyu_dev.views.shuyu_dev2', name='shuyu_home'),
    url(r'^shuyu_dev3/', 'shuyu_dev.views.shuyu_dev3', name='shuyu_home'),


    url(r'^katharine_dev/', 'katharine_dev.views.katharine_dev', name='katharine_home'),
    url(r'^katharine_dev2/', 'katharine_dev.views.katharine_dev2', name='katharine_home'),
    url(r'^katharine_dev3/', 'katharine_dev.views.katharine_dev3', name='katharine_home'),

    url(r'^kang_dev/', 'kang_dev.views.kang_dev', name='kang_home'),
    url(r'^kang_dev2/', 'kang_dev.views.kang_dev2', name='kang_home'),
    url(r'^kang_dev3/', 'kang_dev.views.kang_dev3', name='kang_home'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


