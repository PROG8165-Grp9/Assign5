from django.conf.urls import include, url
from django.contrib import admin
from Users import views

urlpatterns = [
    url(r'^/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^dashboard/$', views.loadItems, name='loadItems'),
]

