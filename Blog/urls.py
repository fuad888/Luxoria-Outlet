from django.urls import path
from Blog import views

urlpatterns = [
    path('blog/', views.Blog_page, name='blogpage'),
    path('blog/<slug:slug>/', views.blog_details, name='blog_details'),
]