from django.contrib import admin
from django.urls import path
from CollegeManagementApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homePage, name="userHomePage"),
    path("signup/", views.signupPage, name="userSignupPage"),
    path("signin/", views.signinPage, name="userSigninPage"),
    path("user-profile/<int:pk>", views.userProfilePage, name="userProfilePage"),
    path("admin-home/", views.adminHomePage, name="adminHomePage"),
    path("add-course/", views.addCoursePage, name="addCoursePage"),
    path("add-student-page/", views.addStudentPage, name="addStudentPage"),
    path("show-student/", views.showStudentsPage, name="showStudentsPage"),
    path("show-teachers/", views.showTeachersPage, name="showTeachersPage"),
    path('show-courses',views.showCourses, name='showCourse'),
    path('edit-student/<int:pk>',views.editStudent, name='editStudent'),
    path('edit-student-data/<int:pk>',views.editStudentData, name='editStudentData'),
    path('remove-course/<int:pk>',views.removeCourse, name='removeCourse'),
    path('edit-course-page/<int:pk>',views.editCoursePage, name='editCoursePage'),
    path('edit-course/<int:pk>',views.editCourse, name='editCourse'),
    
    path("create-user/", views.createUser, name="createUser"),
    path("user-signin/", views.userLogin, name="userLogin"),
    path("user-edit/<int:pk>", views.userProfileEdit, name="userProfileEdit"),
    path("remove-image/<int:pk>", views.removeProfileImage, name="removeImage"),
    path('remove-student-image/<int:pk>',views.removeStudentImage, name='removeStudentImage'),
    path("update-user/<int:pk>", views.updateUserData, name="updateUserData"),
    path("add-course-data/", views.addCourse, name="addCourse"),
    path("add-student-data/", views.addStudentData, name="addStudentData"),
    path("remove-teacher/<int:pk>", views.removeTeacher, name="removeTeacher"),
    path("remove-student/<int:pk>", views.removeStudent, name="removeStudent"),
    path("logout/", views.userLogout, name="userLogout"),
]
