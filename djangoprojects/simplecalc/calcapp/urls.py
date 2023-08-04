from django.contrib import admin
from django.urls import path
from calcapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loadPage, name='loadPage'),
    path('calculate',views.calculate, name='calculate'),
    path('',views.home, name='home'),

]
