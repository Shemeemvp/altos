from django.contrib import admin
from django.urls import path
from UserLoginApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage, name='homePage'),
    path('signup/',views.signupPage, name='signup'),
    path('login/',views.loginPage, name='login'),
    path('about/',views.aboutPage, name='about'),

    path('register-user/',views.registerUser, name='registerUser'),
    path('userlogin/',views.login, name='userlogin'),
    path('logout/',views.logout, name='logout'),
]