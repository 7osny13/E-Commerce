from django.contrib import admin
from django.urls import path
from base.products import products
# from . import views
from base.views import product_views as views
urlpatterns = [
  
    path('', views.getProducts,name="products"),
    path('<str:pk>/', views.getProduct,name="product"),

]
