from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from EcommerceApp.models import CategoryModel, CartModel, CustomerModel, ProductModel
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def homePage(request):
    return render("user/user-home.html")


def signinPage(request):
    return render(request, "login.html")


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


def addCategory(request):
    if request.method == "POST":
        catName = request.POST["category-name"]
        catDesc = request.POST["category-description"]

        category = CategoryModel(category_name=catName, category_description=catDesc)
        category.save()

        messages.success(request, f'{category.category_name} added successfully')
        return redirect("addCategoryPage")


def addProductPage(request):
    category = CategoryModel.objects.all()
    return render(request, 'admin/add-products.html',{'category':category})

def addProductDetails(request):
    if request.method == 'POST':
        pName = request.POST['prod-name']
        pDesc = request.POST['prod-description']
        pPrice = request.POST['prod-price']
        PCategory = CategoryModel.objects.get(id = request.POST['category'])
        pQuantity = request.POST['quantity']
        pMFGDate = request.POST['mfg-date']
        pImage = request.FILES.get('image')

        product = ProductModel(product_name = pName, description = pDesc, category = PCategory, quantity = pQuantity, price = pPrice, mfg_date = pMFGDate, image = pImage)
        product.save()
        messages.info(request, 'Product details added successfully.')

        return redirect('addProductPage')