from django.shortcuts import render

# Create your views here.
def init(request):
    if request.method == "POST":
        name = request.POST.get("x")
        print(name)
    return render(request, 'init.html')