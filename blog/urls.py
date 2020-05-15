
from django.urls import path, include
from . import views

urlpatterns = [
    path('allblogs/', views.allblogs, name = 'post-list'),
    path('post/<id>/', views.detail, name = 'post-detail'),
    path('search/', views.search, name = 'search'),
    path('tinymce/', include('tinymce.urls')),
    path('', views.about, name='about')

    ]
