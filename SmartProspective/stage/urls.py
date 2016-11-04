from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^basic/', views.basic, name='basic'),
    url(r'^database/', views.database, name='database'),
    url(r'^$', views.default, name='default'),
]
