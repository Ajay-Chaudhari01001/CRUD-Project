from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import StudentData

# this function for add new data and shwoing data.
def add_show(request):
     if request.method == 'POST':
       fm = StudentRegistration(request.POST)
       if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            br = fm.cleaned_data['branch']
            pwd = fm.cleaned_data['password']
            reg = StudentData(name=nm, email=em, branch=br, password=pwd)
            reg.save()
            fm = StudentRegistration()
     else:
          fm = StudentRegistration()
     stud = StudentData.objects.all
     return render(request, 'crud/addShow.html', {'form':fm, 'stu':stud })

# This function is use for delete data
def deleteData(request, id):
     if request.method == 'POST':
          pi = StudentData.objects.get(pk=id)
          pi.delete()
          return HttpResponseRedirect('/') 

# this function will update and edit
def updateData(request, id):
     if request.method == 'POST':
          pi = StudentData.objects.get(pk=id)
          fm = StudentRegistration(request.POST, instance=pi)
          if fm.is_valid():
               fm.save()
     else:
          pi = StudentData.objects.get(pk=id)
          fm = StudentRegistration(instance=pi)
     return render(request, 'crud/update.html', {'form':fm})