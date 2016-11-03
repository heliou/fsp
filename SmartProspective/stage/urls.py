from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^basic/', views.basic, name='basic'),
    url(r'^index/', views.index, name='index'),
    url(r'^$', views.default, name='default'),
]
