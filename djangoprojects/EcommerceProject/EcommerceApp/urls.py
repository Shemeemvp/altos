from django.contrib import admin
from django.urls import path
from EcommerceApp import views

urlpatterns = [
    # ADMIN Panel Pages
    path('admin/', admin.site.urls),
    path("admin-home/", views.adminHomePage, name="adminHomePage"),
    path('admin-add-category', views.addCategoryPage, name='addCategoryPage'),
    path('add-category', views.addCategory, name= 'addCategory'),
    path('add-product', views.addProductPage, name='addProductPage'),
    path('add-product-details', views.addProductDetails, name='addProductDetails'),

    # USER AUTHENTICATION
    path("signin/", views.signinPage, name="userSigninPage"),
    path("user-signin/", views.userLogin, name="userLogin"),
    path("logout/", views.userLogout, name="userLogout"),


    
]
