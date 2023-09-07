from django.contrib import admin
from django.urls import path
from EcommerceApp import views

urlpatterns = [

    # Home Page URLs
    path('',views.homePage, name='homePage'),
    path('show-product/<int:pk>',views.showProduct, name= 'showProduct'),

    # ADMIN Panel Pages
    path('admin/', admin.site.urls),
    path("admin-home/", views.adminHomePage, name="adminHomePage"),
    path('admin-add-category', views.addCategoryPage, name='addCategoryPage'),
    path('add-category', views.addCategory, name= 'addCategory'),
    path('show-products/',views.showProducts, name='showProducts'),
    path('add-product', views.addProductPage, name='addProductPage'),
    path('add-product-details', views.addProductDetails, name='addProductDetails'),
    path('edit-product/<int:pk>',views.editProductPage, name='editProductPage'),
    path('edit-product-details/<int:pk>',views.editProductDetails, name='editProductDetails'),
    path('remove-product/<int:pk>',views.removeProduct, name='removeProduct'),
    path('show-categories',views.showCategories, name= 'showCategories'),
    path('edit-category/<int:pk>',views.editCategoryPage, name='editCategoryPage'),
    path('edit-category-details/<int:pk>',views.editCategoryDetails, name= 'editCategoryDetails'),
    path('remove-category/<int:pk>',views.removeCategory, name='removeCategory'),
    path('show-users',views.showUsers, name= 'showUsers'),
    path('remove-user/<int:pk>',views.removeUser, name='removeUser'),
    path('show-orders',views.showOrders, name= 'showOrders'),
    path('dispatch-order/<int:pk>',views.dispatchOrder, name = 'dispatchOrder'),
    path('remove-order/<int:pk>',views.removeOrder, name = 'removeOrder'),
    path('dispatched-orders',views.dispatchedOrders, name = 'dispatchedOrders'),
    path('deliver-order/<int:pk>',views.deliverOrder, name = 'deliverOrder'),

    # GUI Pages
    # CART
    path('cart/',views.userCartPage, name='userCartPage'),
    path('add-to-cart',views.addToCart, name='addToCart'),
    path('remove-cart-item/<int:pk>',views.removeCartItem, name='removeCartItem'),
    path('change-product-quantity',views.changeProductQuantity, name='changeProductQuantity'),
    # CATEGORIES
    path('category-items/<int:pk>',views.showCategoryItems, name='showCategoryItems'),
    path('category-items-all',views.categoryItems, name='categoryItems'),

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
