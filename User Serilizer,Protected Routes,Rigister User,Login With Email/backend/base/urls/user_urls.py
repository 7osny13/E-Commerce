from django.contrib import admin
from django.urls import path
from base.products import products
from base.views import user_views as views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('', views.getRoutes,name="routes"),
    # user profile view only to admin
    path('register/', views.registerUser,name="register"),

    path('profile/', views.getUserprofile,name="users-profile"),
    # all  user profile view only to admin
    path('', views.getusers,name="users"),
   

]
