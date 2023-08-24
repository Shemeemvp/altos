from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.showProducts, name="showProducts"),
    path("add-product", views.addProducts, name="addProducts"),
    path("add-product-item", views.addProductItem, name="addProductItem"),
    path("edit-product/<int:prodId>", views.editProduct, name="editProduct"),
    path(
        "edit-product-item/<int:prodId>", views.editProductItem, name="editProductItem"
    ),
    path("delete-product/<int:prodId>", views.deleteProduct, name="deleteProduct"),
    path("delete-product-item/<int:prodId>", views.deleteItem, name="deleteItem"),
]
