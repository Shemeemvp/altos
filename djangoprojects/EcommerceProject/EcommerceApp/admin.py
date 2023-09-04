from django.contrib import admin
from EcommerceApp.models import CategoryModel, ProductModel

# Register your models here.
@admin.register(CategoryModel)
class CategoryDetailsAdmin(admin.ModelAdmin):
    list_display=('id','category_name','category_description')