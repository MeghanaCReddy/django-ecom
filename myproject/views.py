from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def fashion(request):
    return render(request,'fashion.html')

def healthcare(request):
    return render(request,'healthcare.html')

def grocery(request):
    return render(request,'grocery.html')

def electronic(request):
    return render(request,'electronic.html')

def about(request):
    return render(request,'about.html')