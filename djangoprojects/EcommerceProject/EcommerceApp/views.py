from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from EcommerceApp.models import (
    CategoryModel,
    CartModel,
    CustomerModel,
    ProductModel,
    Orders,
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse


# Create your views here.
def homePage(request):
    ctg = CategoryModel.objects.all()
    prd = ProductModel.objects.all()
    crsl1 = ProductModel.objects.all()[0:4]
    crsl2 = ProductModel.objects.all()[6:10]
    print(crsl1)
    print(crsl2)
    cartItemsCount = len(CartModel.objects.filter(user=request.user.id))
    context = {
        "categories": ctg,
        "count": cartItemsCount,
        "products": prd,
        "crsl1": crsl1,
        "crsl2": crsl2,
    }

    return render(request, "user/products-home.html", context)


def showProduct(request, pk):
    prd = ProductModel.objects.get(id=pk)
    cartItemsCount = len(CartModel.objects.filter(user=request.user.id))
    ctg = CategoryModel.objects.all()
    items = ProductModel.objects.filter(category=prd.category.id)[0:4]
    context = {
        "categories": ctg,
        "count": cartItemsCount,
        "product": prd,
        "items": items,
    }
    return render(request, "user/product.html", context)


# GUI Pages
# CART
@login_required(login_url="userSigninPage")
def userCartPage(request):
    products = CartModel.objects.filter(user=request.user.id)
    netAmount = 0
    for i in products:
        netAmount += i.total_price
    count = len(products)
    ctg = CategoryModel.objects.all()
    context = {
        "categories": ctg,
        "products": products,
        "count": count,
        "sum": netAmount,
    }
    return render(request, "user/cart.html", context)


@login_required(login_url="userSigninPage")
def addToCart(request):
    if request.method == "POST":
        productId = request.POST.get("product")
        item = ProductModel.objects.get(id=productId)
        user = User.objects.get(id=request.user.id)
        if CartModel.objects.filter(user=user.id).exists():
            if (
                CartModel.objects.filter(user=user.id)
                .filter(product=productId)
                .exists()
            ):
                # if product is not None:
                product = CartModel.objects.get(user=user.id, product=productId)
                product.quantity += 1
                product.total_price = product.quantity * product.product.price
                product.save()

                cartItemsCount = len(CartModel.objects.filter(user=request.user.id))
                return JsonResponse(
                    {"status": "Item Added", "cartCount": cartItemsCount}
                )
            else:
                cartItem = CartModel(
                    user=user, product=item, quantity=1, total_price=item.price
                )
                cartItem.save()

                cartItemsCount = len(CartModel.objects.filter(user=request.user.id))
                return JsonResponse(
                    {"status": "Item Added", "cartCount": cartItemsCount}
                )
        else:
            cartItem = CartModel(
                user=user, product=item, quantity=1, total_price=item.price
            )
            cartItem.save()

            cartItemsCount = len(CartModel.objects.filter(user=request.user.id))
            return JsonResponse({"status": "Item Added", "cartCount": cartItemsCount})
    else:
        return redirect("homePage")


def removeCartItem(request, pk):
    cartItem = CartModel.objects.filter(user=request.user.id).filter(product=pk)
    cartItem.delete()
    return redirect("userCartPage")


def changeProductQuantity(request):
    if request.method == "POST":
        prodId = request.POST.get("product")
        count = request.POST.get("count")

        if CartModel.objects.filter(user=request.user.id, product=prodId):
            cart = CartModel.objects.get(user=request.user.id, product=prodId)
            cart.quantity += int(count)
            cart.total_price = cart.quantity * cart.product.price
            cart.save()
            items = CartModel.objects.filter(user=request.user.id)
            netAmount = 0
            for i in items:
                netAmount += i.total_price

            return JsonResponse(
                {"qty": cart.quantity, "totPrice": cart.total_price, "sum": netAmount}
            )
    return redirect("userCartPage")


# CATEGORIES
def showCategoryItems(request, pk):
    items = ProductModel.objects.filter(category_id=pk)
    category = CategoryModel.objects.get(id=pk)
    ctg = CategoryModel.objects.all()
    count = len(CartModel.objects.filter(user=request.user.id))
    context = {"items": items, "category": category, "categories": ctg, "count": count}
    return render(request, "user/categories/category.html", context)


def categoryItems(request):
    items = ProductModel.objects.all()
    ctg = CategoryModel.objects.all()
    count = len(CartModel.objects.filter(user=request.user.id))
    context = {
        "items": items,
        "categoryname": "Products",
        "categories": ctg,
        "count": count,
    }
    return render(request, "user/categories/category.html", context)


# CHECKOUT
def checkoutPage(request):
    customer = CustomerModel.objects.get(user=request.user)
    products = CartModel.objects.filter(user=request.user.id)
    netAmount = 0
    for i in products:
        netAmount += i.total_price
    count = len(products)

    return render(
        request,
        "user/checkout.html",
        {"count": count, "subtotal": netAmount, "customer": customer},
    )


def placeOrder(request):
    if request.method == "POST":
        items = CartModel.objects.filter(user=request.user.id)
        print(items.values())
        for item in items:
            product = ProductModel.objects.get(id=item.product.id)
            quantity = item.quantity
            price = item.total_price
            order = Orders(
                user=User.objects.get(id=request.user.id),
                product=product,
                price=price,
                quantity=quantity,
                payment=request.POST["PaymentMethod"],
                status="Placed",
            )
            order.save()

        cart = CartModel.objects.filter(user=request.user)
        cart.delete()
        items = ProductModel.objects.all()[7:11]
        return render(request, "user/order-placed.html", {"items": items})
    else:
        return redirect("checkoutPage")


# ORDERS
def myOrders(request):
    customer = CustomerModel.objects.get(user=request.user)
    orders = Orders.objects.filter(user=request.user).order_by("-id")
    context = {"orders": orders, "customer": customer}
    return render(request, "user/orders.html", context)


# REGISTER, LOGIN AND LOGOUT


def userSignupPage(request):
    ctg = CategoryModel.objects.all()
    count = len(CartModel.objects.filter(user=request.user.id))
    context = {"categories": ctg, "count": count}
    return render(request, "signup.html", context)


def signinPage(request):
    ctg = CategoryModel.objects.all()
    count = len(CartModel.objects.filter(user=request.user.id))
    context = {"categories": ctg, "count": count}
    return render(request, "login.html", context)


def registerUser(request):
    if request.method == "POST":
        fName = request.POST["first-name"]
        lName = request.POST["last-name"]
        phone = request.POST["mobile"]
        gender = request.POST["gender"]
        address = request.POST["address"]
        uName = request.POST["user-name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if User.objects.filter(username=uName).exists():
            messages.info(request, f"`{uName}` already exists!! Please try another..")
            return redirect("userSignupPage")
        elif User.objects.filter(email=email).exists():
            messages.info(request, f"`{email}` already exists!! Please try another..")
            return redirect("userSignupPage")
        else:
            if password1 == password2:
                userInfo = User.objects.create_user(
                    first_name=fName,
                    last_name=lName,
                    username=uName,
                    email=email,
                    password=password1,
                )
                userInfo.save()

                uData = User.objects.get(id=userInfo.id)
                customerData = CustomerModel(
                    user=uData,
                    gender=gender,
                    phone=phone,
                    address=address,
                )
                customerData.save()
                # messages.info(request, 'Registration Successful..')
                return redirect("userSigninPage")
            else:
                # messages.warning(request, "Passwords doesn't match..Please try again.")
                # return HttpResponse('please! verify your passwords')
                return redirect("userSignupPage")
    else:
        return redirect("userSignupPage")


def userLogin(request):
    try:
        next = request.GET.get("next")
    except:
        pass
    if request.method == "POST":
        uName = request.POST["user-name"]
        password = request.POST["password"]

        user = auth.authenticate(username=uName, password=password)
        if user is not None:
            if user.is_staff:
                auth.login(request, user)
                return redirect("adminHomePage")
                # return render(request, "admin-home.html", {"user": request.user})
            else:
                auth.login(request, user)
                if next:
                    return redirect(next)
                return redirect("homePage")
        else:
            messages.info(request, "Incorrect Username or Password..Please try again")
            return redirect("userSigninPage")
    else:
        return redirect("userSigninPage")


@login_required(login_url="userSigninPage")
def userLogout(request):
    auth.logout(request)
    return redirect("userSigninPage")


# ADMIN Panel Pages and Functions


@login_required(login_url="userSigninPage")
def adminHomePage(request):
    vendors = len(ProductModel.objects.all().values('vendor').distinct())
    customers = len(CustomerModel.objects.all())
    print(vendors)
    orders = len(Orders.objects.filter(status="Placed"))
    products = len(ProductModel.objects.all())
    items = Orders.objects.filter(status="Delivered")
    sales = len(Orders.objects.filter(status="Delivered"))
    revenue = 0
    for i in items:
        revenue += i.price
    context = {
        "orders": orders,
        "products": products,
        "sales": sales,
        "revenue": revenue,
        "user": request.user,
        'customers':customers,
        "sellers":vendors
    }
    return render(request, "admin/admin-home.html", context)


def addCategoryPage(request):
    return render(request, "admin/add-category.html")


@login_required(login_url="userSigninPage")
def addCategory(request):
    if request.method == "POST":
        catName = request.POST["category-name"]
        catDesc = request.POST["category-description"]

        category = CategoryModel(category_name=catName, category_description=catDesc)
        category.save()

        messages.success(request, f"{category.category_name} added successfully")
        return redirect("showCategories")


def addProductPage(request):
    category = CategoryModel.objects.all()
    return render(request, "admin/add-products.html", {"category": category})


@login_required(login_url="userSigninPage")
def showProducts(request):
    products = ProductModel.objects.all()
    return render(request, "admin/show-products.html", {"products": products})


@login_required(login_url="userSigninPage")
def removeProduct(request, pk):
    item = ProductModel.objects.get(id=pk)
    item.delete()
    messages.success(request, "Product Removed Successfully")
    return redirect("showProducts")


@login_required(login_url="userSigninPage")
def addProductDetails(request):
    if request.method == "POST":
        pName = request.POST["prod-name"]
        pDesc = request.POST["prod-description"]
        pPrice = request.POST["prod-price"]
        pListPrice = request.POST["original-price"]
        PCategory = CategoryModel.objects.get(id=request.POST["category"])
        pQuantity = request.POST["quantity"]
        pMFGDate = request.POST["mfg-date"]
        vendor = request.POST["vendor"]
        pImage = request.FILES.get("image")

        product = ProductModel(
            product_name=pName,
            description=pDesc,
            category=PCategory,
            quantity=pQuantity,
            price=pPrice,
            original_price=pListPrice,
            mfg_date=pMFGDate,
            vendor=vendor,
            image=pImage,
        )
        product.save()
        messages.info(request, "Product details added successfully.")

        return redirect("showProducts")


@login_required(login_url="userSigninPage")
def editProductPage(request, pk):
    category = CategoryModel.objects.all()
    product = ProductModel.objects.get(id=pk)
    return render(
        request, "admin/edit-products.html", {"product": product, "category": category}
    )


@login_required(login_url="userSigninPage")
def editProductDetails(request, pk):
    product = ProductModel.objects.get(id=pk)
    if request.method == "POST":
        pName = request.POST["prod-name"]
        pDesc = request.POST["prod-description"]
        pPrice = request.POST["prod-price"]
        pListPrice = request.POST["original-price"]
        PCategory = CategoryModel.objects.get(id=request.POST["category"])
        pQuantity = request.POST["quantity"]
        pMFGDate = request.POST["mfg-date"]
        vendor = request.POST["vendor"]
        newImage = request.FILES.get("image")
        currentImage = product.image
        if newImage is not None:
            product.image = newImage
        else:
            product.image = currentImage
        product.product_name = pName
        product.description = pDesc
        product.price = pPrice
        product.original_price = pListPrice
        product.category = PCategory
        product.quantity = pQuantity
        product.mfg_date = pMFGDate
        product.vendor = vendor
        product.save()

        messages.info(request, "Details Updated Successfully.")
        return redirect("showProducts")
    else:
        return redirect("editProductPage", pk)


def showUsers(request):
    users = CustomerModel.objects.all()
    return render(request, "admin/view-users.html", {"user": users})


def showCategories(request):
    categories = CategoryModel.objects.all()
    return render(request, "admin/show-categories.html", {"categories": categories})


def editCategoryPage(request, pk):
    category = CategoryModel.objects.get(id=pk)
    return render(request, "admin/edit-category.html", {"category": category})


def editCategoryDetails(request, pk):
    if request.method == "POST":
        cName = request.POST["category-name"]
        cDesc = request.POST["category-description"]

        category = CategoryModel.objects.get(id=pk)
        category.category_name = cName
        category.category_description = cDesc
        category.save()
        messages.info(request, "Category Details updated successfully.")
        return redirect("showCategories")
    else:
        return redirect("showCategories")


def removeCategory(request, pk):
    category = CategoryModel.objects.get(id=pk)
    category.delete()

    messages.info(request, "Category Removed")
    return redirect("showCategories")


def showUsers(request):
    users = CustomerModel.objects.all()
    return render(request, "admin/show-users.html", {"users": users})


def removeUser(request, pk):
    user = CustomerModel.objects.get(id=pk)
    auth = User.objects.get(id=user.user.id)
    auth.delete()
    user.delete()
    messages.info(request, "User Details Removed")

    return redirect("showUsers")


def showOrders(request):
    orders = Orders.objects.all().order_by("-id")
    return render(request, "admin/show-orders.html", {"orders": orders})


def dispatchOrder(request, pk):
    item = Orders.objects.get(id=pk)
    item.status = "Dispatched"
    item.save()

    messages.info(request, f"Order {item.id} dispatched.")
    return redirect("showOrders")


def removeOrder(request, pk):
    order = Orders.objects.get(id=pk)
    order.delete()
    messages.info(request, "Order Removed")
    return redirect("showOrders")


def dispatchedOrders(request):
    orders = Orders.objects.filter(status="Dispatched")
    return render(request, "admin/dispatched-orders.html", {"orders": orders})


def deliverOrder(request, pk):
    item = Orders.objects.get(id=pk)
    item.status = "Delivered"
    item.save()
    messages.info(request, "Order Marked as Delivered!")

    return redirect("dispatchedOrders")
