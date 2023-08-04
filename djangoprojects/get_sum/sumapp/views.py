from django.shortcuts import render

# Create your views here.
def addNumbers(request):
    return render(request, 'addnum.html')

def getSum(request):
    num1 = int(request.GET.get('number1'))
    num2 = int(request.GET.get('number2'))
    sum = num1+num2
    return render(request, 'sum.html',{'result':sum})

'''def getSum(request):
    # num1 = int(request.GET.get('number1'))
    # num2 = int(request.GET.get('number2'))
    # sum = num1+num2
    return render(request, 'sum.html')'''