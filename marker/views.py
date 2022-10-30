from django.shortcuts import render, redirect
from .models import imageUpload
from .forms import photoUpload
from django.contrib import messages

# Create your views here.

def home(request):
    image = imageUpload.objects.all().order_by('-date_uploaded')
    context = {'image':image}
    return render(request, 'marker/home.html', context)



def upload(request):
    form = photoUpload()
    if request.method == 'POST':
        form = photoUpload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Upload Successful!')
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'marker/upload.html', context)