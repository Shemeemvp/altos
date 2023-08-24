from django.contrib import admin
from django.urls import path
from SecondApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome',views.welcomePage, name='welcomePage'),
]