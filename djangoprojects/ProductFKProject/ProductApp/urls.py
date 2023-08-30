from django.contrib import admin
from django.urls import path
from ProductApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='homePage'),
    path('add-categories-page', views.addCategoriesPage, name='addCategoriesPage'),
    path('add-product-page', views.addProductPage, name='addProductPage'),
    path('products', views.productsPage, name='productsPage'),
    path('tables', views.tablesPage, name='tablesPage'),
    path('empty-products', views.emptyProducts, name='emptyProducts'),

    path('add-category', views.addCategory, name='addCategory'),
    path('add-product', views.addProduct, name='addProduct'),
    path('remove-product/<int:pk>', views.removeProduct, name='removeProduct'),
]