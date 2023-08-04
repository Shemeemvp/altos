from django.shortcuts import render


# Create your views here.
def loadPage(request):
    return render(request, "calculate.html")


def calculate(request):
    res = ""
    try:
        if request.method == "POST":
            value1 = int(request.POST.get("num1"))
            value2 = int(request.POST.get("num2"))
            op = request.POST.get("operand")

            if op == "+":
                res = value1 + value2
            elif op == "-":
                res = value1 - value2
            elif op == "*":
                res = value1 * value2
            elif op == "/":
                res = value1 / value2
    except:
        res = "Invalid"
    # print(res)
    return render(request, "calculate.html", {"result": res})

def home(request):
    return render(request,'calculate.html')