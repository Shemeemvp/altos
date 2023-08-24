from django.contrib import admin
from django.urls import path
from StdRegApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("enroll", views.enrollStudent, name="enrollStudent"),
    path("enroll-data", views.enrollStudentData, name="enrollStudentData"),
    path("edit-student/<int:pk>", views.editStudent, name="editStudent"),
    path("edit-student-data/<int:pk>", views.editStudentData, name="editStudentData"),
    path("delete-student/<int:pk>", views.deleteStudent, name="deleteStudent"),
    path("view-profile/<int:pk>", views.viewProfile, name="viewProfile"),
]
