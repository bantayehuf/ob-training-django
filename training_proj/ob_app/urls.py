from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('/welcome', views.sample_template, name='welcome'),
    path('/blog', views.blog_mgt, name='blog'),
]
