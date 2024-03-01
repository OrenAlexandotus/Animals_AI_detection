from django.shortcuts import render, redirect
from .forms import ImageForm

# Create your views here.

def index(request):
    return render(request, "index.html")

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')