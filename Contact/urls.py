from django.urls import path
from Contact import views


urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('subscribe/', views.subscribe, name='subscribe'),
]