from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name = "detail"),
    path('create', views.create, name = "create"),
    path('new/', views.new, name = "new"),
    path('newblog/', views.blogpost, name = "newblog"),
    path('blog/', views.blog, name = "blog"),
    path('plus/', views.plus, name = "plus"),
    path('search/', views.search, name = "search"),
]