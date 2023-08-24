from django.shortcuts import render, redirect
from StdRegApp.models import StudentData
from django.contrib import messages


# Create your views here.
def home(request):
    students_data = StudentData.objects.all().values()
    # print('============student Data=============')
    # print(students_data.values('image'))
    if not students_data:
        return render(request, "empty-home.html")
    else:
        return render(request, "home.html", {"std": students_data})


def enrollStudent(request):
    return render(request, "enroll.html")


def enrollStudentData(request):
    if request.method == "POST":
        fName = request.POST["first-name"]
        lName = request.POST["last-name"]
        phone = request.POST["phone-number"]
        email = request.POST["email"]
        course = request.POST["course"]
        address = request.POST["address"]
        # image = request.FILES["image"]
        image = request.FILES.get("image")

        stdData = StudentData(
            first_name=fName,
            last_name=lName,
            phone_number=phone,
            email=email,
            course=course,
            address=address,
            image=image,
        )
        stdData.save()
        messages.success(request, "Student details added successfully.")
        return redirect("home")


def viewProfile(request, pk):
    stdData = StudentData.objects.get(id=pk)
    return render(request, "profile.html", {"student": stdData})


def editStudent(request, pk):
    stdData = StudentData.objects.get(id=pk)
    return render(request, "edit.html", {"std": stdData})


def editStudentData(request, pk):
    if request.method == "POST":
        stdData = StudentData.objects.get(id=pk)
        newImage = request.FILES.get('image')
        currentImage = stdData.image
        photoTrue = request.POST['checkphoto']
        print('phototrue')
        print(photoTrue)
        if newImage is not None:
            stdData.image = newImage
        elif photoTrue == 'false':
            stdData.image = None
        else:
            stdData.image = currentImage
        stdData.first_name = request.POST["first-name"]
        stdData.last_name = request.POST["last-name"]
        stdData.phone_number = request.POST["phone-number"]
        stdData.email = request.POST["email"]
        stdData.course = request.POST["course"]
        stdData.address = request.POST["address"]

        stdData.save()
        messages.success(request, "Student Details updated successfully.")
        return render(request, "profile.html", {"student": stdData})


def deleteStudent(request, pk):
    stdData = StudentData.objects.get(id=pk)
    stdData.delete()

    return redirect("home")
