
from django.urls import path, include
from . import views

urlpatterns = [
    path('allblogs/', views.allblogs, name = 'post-list'),
    path('post/<slug:slug>/', views.detail, name = 'post-detail'),
    path('search/', views.search, name = 'search'),
    path('Videos', views.Video_cat, name = 'Videos'),

    path('Category', views.Categories, name = 'Category'),
    path('CategoryList/<str:categories>', views.Cat_list, name = 'CategoryList'),

    path('', views.about, name='about')

    ]
