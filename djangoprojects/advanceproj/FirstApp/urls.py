from django.contrib import admin
from django.urls import path
from FirstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indexPage, name='indexPage'),
    path('homepage',views.homePage, name='homePage'),
]