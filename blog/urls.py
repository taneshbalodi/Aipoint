
from django.urls import path, include
from . import views

urlpatterns = [
    path('allblogs/', views.allblogs, name = 'post-list'),
    path('post/<slug:slug>/', views.detail, name = 'post-detail'),
    path('search/', views.search, name = 'search'),

    path('', views.about, name='about')

    ]
