from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .forms import FileUploadForm
from .models import UploadedFile


@login_required
def home(request):
    files = UploadedFile.objects.all()

    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'File uploaded successfully!')
            return redirect('base:home')  # Redirect to the same page to show the success message
        else:
            messages.error(request, 'Error uploading file. Please try again.')

    else:
        form = FileUploadForm()

    return render(request, "home.html", {"form": form, "files": files})

def delete_file(request, file_id):
    # Retrieve the file object based on the file_id
    file = get_object_or_404(UploadedFile, id=file_id)
    
    # Delete the file from the storage and remove from the database
    file.delete()
    
    # Provide feedback to the user
    messages.success(request, "File deleted successfully.")
    
    # Redirect back to the file upload page or a specific page after deletion
    return redirect('base:home')  # Change this to the URL name of your file upload page


def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("base:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})
