from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Image

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')

    form = ImageForm()
    return render(request, 'upload_form.html',{'form':form})


def image_list(request):
    images=Image.objects.all()
    return render(request, "image_list.html", {"images":images})


def deleteImage(request,pk):
    try:
        Image.objects.get(pk=pk).delete()
    except Exception as e:
        pass
    return redirect("image_list")

