from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse


# Create your views here.
def homePage(request):
    return render(request, "home.html")


def signupPage(request):
    return render(request, "signup.html")


def loginPage(request):
    return render(request, "login.html")


@login_required(login_url='login')
def aboutPage(request):
    return render(request, "about.html")


def registerUser(request):
    if request.method == "POST":
        fName = request.POST["first-name"]
        lName = request.POST["last-name"]
        uName = request.POST["user-name"]
        email = request.POST["email"]
        password = request.POST["password1"]
        re_password = request.POST["password2"]

        if User.objects.filter(username=uName).exists():
            messages.info(request, "Username already exists!! Please try another..")
            return redirect("signup")
        else:
            if password == re_password:
                userInfo = User.objects.create_user(
                    first_name=fName,
                    last_name=lName,
                    username=uName,
                    email=email,
                    password=password,
                )
                userInfo.save()
                # messages.info(request, 'Registration Successful..')
                print("=============Registration successful============")
                return redirect("login")
            else:
                # messages.warning(request, "Passwords doesn't match..Please try again.")
                print("=========Password does not match=======")
                # return HttpResponse('please! verify your passwords')
                return redirect("signup")
    else:
        return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        uName = request.POST["user-name"]
        pWord = request.POST["password"]

        user = auth.authenticate(username=uName, password=pWord)
        if user is not None:
            auth.login(request, user)
            return render(request, 'about.html', {'user':request.user})
        else:
            messages.info(request, "Incorrect Username or Password..Please try again")
            return redirect("login")
    else:
        return render(request, "login.html")

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')