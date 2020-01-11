from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import Template,Context 
from django.views.generic import TemplateView, ListView, CreateView
from .models import Student
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import BookForm
from .models import Book

def view_hello_world_test(request):
    return render(request,'students/test.html')

def view_student_lists(request):
    list_of_students= Student.objects.all()
    print(list_of_students)
    context_variable = {
        'student':list_of_students
    }
    return render(request,'students/student.html',context_variable)

def view_student_page(request):
    return render(request,'students/student.html')

def view_student_form(request):
    return render(request,'students/create.html')

def view_studentdata_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_first_Name = request.POST['first_Name']
        print(type(get_first_Name))
        get_last_Name = request.POST['last_Name']
        get_Phoneno = request.POST['Phoneno']
        get_Address = request.POST['Address']
        print(get_first_Name)
        students_obj = Student(first_Name=get_first_Name,last_Name=get_last_Name,Phoneno=get_Phoneno,Address=get_Address)
        students_obj.save()
        return HttpResponse("Record Saved")
    else:
        return HttpResponse("Error record saving")