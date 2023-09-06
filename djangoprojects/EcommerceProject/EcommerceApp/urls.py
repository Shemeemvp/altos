from django.contrib import admin
from django.urls import path
from EcommerceApp import views

urlpatterns = [

    # Home Page URLs
    path('',views.homePage, name='homePage'),

    # ADMIN Panel Pages
    path('admin/', admin.site.urls),
    path("admin-home/", views.adminHomePage, name="adminHomePage"),
    path('admin-add-category', views.addCategoryPage, name='addCategoryPage'),
    path('add-category', views.addCategory, name= 'addCategory'),
    path('show-products/',views.showProducts, name='showProducts'),
    path('add-product', views.addProductPage, name='addProductPage'),
    path('add-product-details', views.addProductDetails, name='addProductDetails'),
    path('remove-product/<int:pk>',views.removeProduct, name='removeProduct'),

    # GUI Pages
    # CART
    path('cart/',views.userCartPage, name='userCartPage'),
    path('add-to-cart',views.addToCart, name='addToCart'),
    path('remove-cart-item/<int:pk>',views.removeCartItem, name='removeCartItem'),
    path('change-product-quantity',views.changeProductQuantity, name='changeProductQuantity'),
    # CATEGORIES
    path('category-items/<int:pk>',views.showCategoryItems, name='showCategoryItems'),

    # Checkout
    path('checkout/',views.checkoutPage, name='checkoutPage'),
    path('place-order/',views.placeOrder, name='placeOrder'),

    # My Orders
    path('my-orders/',views.myOrders, name='myOrders'),

    # USER AUTHENTICATION
    path('signup/',views.userSignupPage, name='userSignupPage'),
    path('register-user/',views.registerUser, name='registerUser'),
    path("signin/", views.signinPage, name="userSigninPage"),
    path("user-signin/", views.userLogin, name="userLogin"),
    path("logout/", views.userLogout, name="userLogout"),
    
]
