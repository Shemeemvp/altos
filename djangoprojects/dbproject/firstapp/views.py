from django.shortcuts import render, redirect
from firstapp.models import ProductDetails


# Create your views here.
def showProducts(request):
    products = ProductDetails.objects.all().values()
    print(products)
    if not products:
        return render(request, "empty-products.html")
    else:
        return render(request, "products.html", {"product": products})


def addProducts(request):
    return render(request, "addProduct.html")


def addProductItem(request):
    if request.method == "POST":
        prName = request.POST["product-name"]
        prDesc = request.POST["product-desc"]
        prQnty = request.POST["product-qnty"]
        prPrice = request.POST["product-price"]

        product = ProductDetails(
            product_name=prName, description=prDesc, quantity=prQnty, price=prPrice
        )

        product.save()
        return redirect("showProducts")
    return render(request, "addProduct.html")


def editProduct(request, prodId):
    productDetails = ProductDetails.objects.get(id=prodId)
    return render(request, "editProduct.html", {"product": productDetails})


def deleteProduct(request, prodId):
    productDetails = ProductDetails.objects.get(id=prodId)
    return render(request, "deleteProduct.html", {"product": productDetails})


def editProductItem(request, prodId):
    if request.method == "POST":
        products = ProductDetails.objects.get(id=prodId)
        products.product_name = request.POST["product-name"]
        products.description = request.POST["product-desc"]
        products.quantity = request.POST["product-qnty"]
        products.price = request.POST["product-price"]

        products.save()

        return redirect("showProducts")
    return render(request, "editProduct.html")


def deleteItem(request, prodId):
    product = ProductDetails.objects.get(id=prodId)
    product.delete()

    return redirect("showProducts")
