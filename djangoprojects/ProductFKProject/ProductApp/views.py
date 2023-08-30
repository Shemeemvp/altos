from django.shortcuts import render, redirect
from ProductApp.models import CategoriesModel, ProductModel
from django.contrib import messages


# Create your views here.
def homePage(request):
    return render(request, "home.html")


def addCategoriesPage(request):
    return render(request, "add_categories.html")


def addProductPage(request):
    categories = CategoriesModel.objects.all()

    return render(request, "add_products.html", {"categories": categories})


def emptyProducts(request):
    return render(request, "empty-products.html")


def productsPage(request):
    products = ProductModel.objects.all()
    if not products:
        return redirect("emptyProducts")

    return render(request, "products.html", {"productData": products})


def tablesPage(request):
    products = ProductModel.objects.all()
    categories = CategoriesModel.objects.all()

    return render(
        request, "tables.html", {"productData": products, "categories": categories}
    )


def addCategory(request):
    if request.method == "POST":
        categoryName = request.POST["category-name"]

        category = CategoriesModel(category_name=categoryName)
        category.save()
        messages.info(request, "Category added Successfully")
        return redirect("tablesPage")


def addProduct(request):
    if request.method == "POST":
        prodName = request.POST["prod-name"]
        option = request.POST["prod-category"]
        prodCategory = CategoriesModel.objects.get(id=option)
        prodDesc = request.POST["prod-description"]
        prodQuantity = request.POST["prod-quantity"]
        prodPrice = request.POST["prod-price"]
        prodMFGDate = request.POST["prod-manufacture-date"]
        prodImage = request.FILES.get("image")

        product = ProductModel(
            product_name=prodName,
            product_description=prodDesc,
            product_quantity=prodQuantity,
            product_price=prodPrice,
            product_manufacture_date=prodMFGDate,
            product_image=prodImage,
            product_category=prodCategory,
        )
        product.save()
        messages.info(request, "Item added successfully.")

        return redirect("productsPage")
    return redirect("addProductPage")


def removeProduct(request, pk):
    product = ProductModel.objects.get(id=pk)
    product.delete()
    # messages.info(request, 'Item removed successfully.')

    return redirect("productsPage")
