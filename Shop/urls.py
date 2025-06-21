from django.urls import path
from Shop import views

urlpatterns = [
    path('shop/', views.Shop, name='shop'),
    path('product_detail/<slug:slug>/', views.product_detail, name='shop-details'),
]