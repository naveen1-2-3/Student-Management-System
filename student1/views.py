from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.urls import reverse

# Create your views here.
def create_view(request):
    if request.POST:
        stuname = request.POST.get("stuname")
        stuage = request.POST.get("stuage")
        sturno = request.POST.get("sturno")
        print(stuname,stuage,sturno)
        models.student1.objects.create(stuname = stuname,stuage=stuage,sturno=sturno)
        return redirect(reverse("student1:show"))
    else:
        return render(request,"student1/create.html")

def show_view(request):
    allstudent= models.student1.objects.all()
    context = {"allstudent":allstudent}
    return render(request,"student1/show.html",context=context)

def update_view(request,pk):
    student = models.student1.objects.get(id=pk)
    if student is None:
        return HttpResponse("student not found")
    if request.method == "POST":
        stuname = request.POST.get("stuname")
        stuage = request.POST.get("stuage")
        sturno = request.POST.get("sturno")
        student.stuname = stuname
        student.stuage = stuage
        student.sturno = sturno
        student.save()
        return redirect(reverse("student1:show"))
    else:
        context = {"student":student}
        return render(request,"student1/update.html",context=context)

def delete_view(request,pk):
    student = models.student1.objects.get(id=pk)
    if request.method == "POST":
        models.student1.objects.get(id=pk).delete()
        return redirect(reverse("student1:show"))

    return render(request,"student1/delete.html",{"student":student})

