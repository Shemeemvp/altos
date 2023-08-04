from django.shortcuts import render

# Create your views here.


def homePage(request):
    return render(request, "home.html")


def pageEkm(request):
    return render(request, "ernakulam.html")


def pageAlp(request):
    return render(request, "alappuzha.html")


def pageIdukki(request):
    return render(request, "idukki.html")


def pageTvm(request):
    return render(request, "trivandrum.html")


def pageWayanad(request):
    return render(request, "wayanad.html")
