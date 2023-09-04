from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from EcommerceApp.models import CategoryModel, CartModel, CustomerModel, ProductModel
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def homePage(request):
    return render(request, "user/products-home.html")


# GUI Pages
def userCartPage(request):
    return render(request, "user/cart.html")


def userSignupPage(request):
    return render(request, "signup.html")


def signinPage(request):
    return render(request, "login.html")


# REGISTER, LOGIN AND LOGOUT
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
                # userDetails = TeacherModel.objects.get(teacher_info=user.id)
                return redirect("userProfilePage", user.id)
                # return render(
                #     request,
                #     "user-profile.html",
                #     {"user": request.user, "userDetails": userDetails},
                # )
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
    return render(request, "admin/admin-home.html", {"user": request.user})


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
        return redirect("addCategoryPage")


def addProductPage(request):
    category = CategoryModel.objects.all()
    return render(request, "admin/add-products.html", {"category": category})


@login_required(login_url="userSigninPage")
def addProductDetails(request):
    if request.method == "POST":
        pName = request.POST["prod-name"]
        pDesc = request.POST["prod-description"]
        pPrice = request.POST["prod-price"]
        PCategory = CategoryModel.objects.get(id=request.POST["category"])
        pQuantity = request.POST["quantity"]
        pMFGDate = request.POST["mfg-date"]
        pImage = request.FILES.get("image")

        product = ProductModel(
            product_name=pName,
            description=pDesc,
            category=PCategory,
            quantity=pQuantity,
            price=pPrice,
            mfg_date=pMFGDate,
            image=pImage,
        )
        product.save()
        messages.info(request, "Product details added successfully.")

        return redirect("addProductPage")


def showUsers(request):
    users = CustomerModel.objects.all()
    return render(request, "admin/view-users.html", {"user": users})
