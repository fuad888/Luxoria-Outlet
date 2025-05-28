from django.urls import path
from Home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog-details/<slug:slug>/', views.blog_details, name='blog_details'),
    path('search/', views.Search, name='search'),
]