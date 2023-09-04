from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from CollegeManagementApp.models import CourseModel, TeacherModel, StudentModel


# Create your views here.
def homePage(request):
    return render(request, "user-home.html")


def signupPage(request):
    courses = CourseModel.objects.all()
    return render(request, "user-signup.html", {"courses": courses})


def signinPage(request):
    return render(request, "user-login.html")


@login_required(login_url="userSigninPage")
def userProfilePage(request, pk):
    userData = TeacherModel.objects.get(teacher_info=pk)
    return render(
        request, "user-profile.html", {"user": request.user, "userDetails": userData}
    )


@login_required(login_url="userSigninPage")
def adminHomePage(request):
    return render(request, "admin-home.html", {"user": request.user})


def addCoursePage(request):
    return render(request, "admin-addcourse.html")


def addStudentPage(request):
    courses = CourseModel.objects.all()
    return render(request, "admin-addstudent.html", {"courses": courses})

def editStudent(request, pk):
    courses = CourseModel.objects.all()
    student = StudentModel.objects.get(id = pk)
    return render(request, 'admin-editstudent.html',{"courses": courses, 'student':student})

@login_required(login_url="userSigninPage")
def showStudentsPage(request):
    students = StudentModel.objects.all()
    return render(request, "admin-showstudent.html", {"students": students})

@login_required(login_url="userSigninPage")
def showTeachersPage(request):
    teachers = TeacherModel.objects.all()
    return render(request, "admin-showteacher.html", {"teachers": teachers})

def showCourses(request):
    courses = CourseModel.objects.all()
    return render(request, 'admin-showcourse.html',{'courses':courses})

def editCoursePage(request, pk):
    crs = CourseModel.objects.get(id = pk)
    return render(request, 'admin-editcourse.html', {'course':crs})

def removeCourse(request, pk):
    course = CourseModel.objects.get(id = pk)
    course.delete()
    return redirect('showCourse')


def createUser(request):
    if request.method == "POST":
        fName = request.POST["first-name"]
        lName = request.POST["last-name"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        phone = request.POST["mobile"]
        crsSelect = request.POST["course"]
        course = CourseModel.objects.get(id=crsSelect)
        address = request.POST["address"]
        image = request.FILES.get("image")
        uName = request.POST["user-name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if User.objects.filter(username=uName).exists():
            messages.info(request, "Username already exists!! Please try another..")
            return redirect("userSignupPage")
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email ID already exists!! Please try another..")
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
                teacherData = TeacherModel(
                    teacher_info=uData,
                    age=age,
                    gender=gender,
                    phone=phone,
                    course=course,
                    address=address,
                    image=image,
                )
                teacherData.save()
                # messages.info(request, 'Registration Successful..')
                print("=============Registration successful============")
                return redirect("userSigninPage")
            else:
                # messages.warning(request, "Passwords doesn't match..Please try again.")
                print("=========Password does not match=======")
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
                userDetails = TeacherModel.objects.get(teacher_info=user.id)
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

@login_required(login_url="userSigninPage")
def userProfileEdit(request, pk):
    user = User.objects.get(id=pk)
    details = TeacherModel.objects.get(teacher_info=pk)
    courses = CourseModel.objects.all()
    context = {"user": user, "userDetails": details, "courses": courses}
    return render(request, "user-edit.html", context)

@login_required(login_url="userSigninPage")
def removeProfileImage(request, pk):
    userDetails = TeacherModel.objects.get(teacher_info=pk)
    userDetails.image = None
    userDetails.save()

    user = User.objects.get(id=pk)
    details = TeacherModel.objects.get(teacher_info=pk)
    courses = CourseModel.objects.all()
    context = {"user": user, "userDetails": details, "courses": courses}
    return render(request, "user-edit.html", context)

@login_required(login_url="userSigninPage")
def removeStudentImage(request, pk):
    student = StudentModel.objects.get(id=pk)
    student.image = None
    student.save()

    courses = CourseModel.objects.all()
    context = {"student": student, "courses": courses}
    return render(request, "admin-editstudent.html", context)

@login_required(login_url="userSigninPage")
def updateUserData(request, pk):
    if request.method == "POST":
        user = User.objects.get(id=pk)
        userDetails = TeacherModel.objects.get(teacher_info=pk)

        fName = request.POST["first-name"]
        lName = request.POST["last-name"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        phone = request.POST["mobile"]
        crsSelect = request.POST["course"]
        course = CourseModel.objects.get(id=crsSelect)
        address = request.POST["address"]
        # image = request.FILES.get("image")
        uName = request.POST["user-name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if user.username != uName:
            if User.objects.filter(username=uName).exists():
                messages.info(request, "Username already exists!! Please try another..")
                return redirect("userProfileEdit", pk)
            else:
                user.username = uName
                user.save()
                return redirect("userProfilePage", pk)
        elif user.email != email:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email ID already exists!! Please try another..")
                return redirect("userProfileEdit", pk)
            else:
                user.email = email
                user.save()
                return redirect("userProfilePage", pk)
        else:
            user.first_name = fName
            user.last_name = lName
            # user.username = uName
            # user.email = email
            user.save()

            

            newImage = request.FILES.get("image")
            currentImage = userDetails.image
            if newImage is not None:
                userDetails.image = newImage
            else:
                userDetails.image = currentImage
            userDetails.age = age
            userDetails.address = address
            userDetails.gender = gender
            userDetails.course = course
            userDetails.phone = phone
            userDetails.save()
            # messages.info(request, 'Registration Successful..')
            print("=============User updation successful============")
            return redirect("userProfilePage", pk)
    else:
        return redirect("userProfileEdit", pk)

@login_required(login_url="userSigninPage")
def addCourse(request):
    if request.method == "POST":
        cName = request.POST["course-name"]
        cDuration = request.POST["course-duration"]
        cFee = request.POST["course-fee"]

        courseData = CourseModel(
            course_name=cName, course_duration=cDuration, course_fee=cFee
        )
        courseData.save()
        return redirect("showCourse")
    
@login_required(login_url="userSigninPage")
def editCourse(request, pk):
    if request.method == "POST":
        cName = request.POST["course-name"]
        cDuration = request.POST["course-duration"]
        cFee = request.POST["course-fee"]

        courseData = CourseModel.objects.get(id = pk)
        courseData.course_name = cName
        courseData.course_duration = cDuration
        courseData.course_fee = cFee
        courseData.save()
        return redirect("showCourse")

@login_required(login_url="userSigninPage")
def addStudentData(request):
    if request.method == "POST":
        fName = request.POST["first-name"]
        lName = request.POST["last-name"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        email = request.POST["email"]
        phone = request.POST["mobile"]
        crsSelect = request.POST["course"]
        course = CourseModel.objects.get(id=crsSelect)
        address = request.POST["address"]
        image = request.FILES.get("image")

        student = StudentModel(
            first_name=fName,
            last_name=lName,
            age=age,
            gender=gender,
            email=email,
            phone=phone,
            course=course,
            address=address,
            image=image,
        )
        student.save()
        return redirect("addStudentPage")
    

@login_required(login_url="userSigninPage")
def editStudentData(request,pk):
    if request.method == "POST":
        fName = request.POST["first-name"]
        lName = request.POST["last-name"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        email = request.POST["email"]
        phone = request.POST["mobile"]
        crsSelect = request.POST["course"]
        course = CourseModel.objects.get(id=crsSelect)
        address = request.POST["address"]

        student = StudentModel.objects.get(id = pk)
        newImage = request.FILES.get("image")
        currentImage = student.image
        if newImage is not None:
            student.image = newImage
        else:
            student.image = currentImage
        student.first_name = fName
        student.last_name = lName
        student.age = age
        student.gender = gender
        student.email = email
        student.phone = phone
        student.course = course
        student.address = address

        student.save()
        return redirect("showStudentsPage")

@login_required(login_url="userSigninPage")
def removeTeacher(request, pk):
    teacher = TeacherModel.objects.get(id=pk)
    userAuthDetails = teacher.teacher_info.id
    teacher.delete()
    user = User.objects.get(id=userAuthDetails)
    user.delete()

    return redirect("showTeachersPage")

@login_required(login_url="userSigninPage")
def removeStudent(request, pk):
    student = StudentModel.objects.get(id=pk)
    student.delete()

    return redirect("showStudentsPage")
