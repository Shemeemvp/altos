from django.contrib import admin
from django.urls import path
from sumapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.addNumbers, name='addNumbers'),
    path('getsum',views.getSum,name='getSum')

]
