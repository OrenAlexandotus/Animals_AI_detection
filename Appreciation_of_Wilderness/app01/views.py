from django.shortcuts import render

# Create your views here.
def init(request):

    return render(request, 'init.html')

def login(request):

    return render(request, 'login.html')

def reset(request):

    return render(request, 'reset.html')

def find(request):

    return render(request, 'find.html')