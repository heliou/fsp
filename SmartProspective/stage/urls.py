from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^basic/', views.basic, name='basic'),
    url(r'^variable/', views.variable, name='variable'),
    url(r'^$', views.default, name='default'),
]
