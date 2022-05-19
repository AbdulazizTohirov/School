from tkinter import E
from django.shortcuts import redirect, render
from .models import *


def index_view(request):
    teachers = TeacherModel.objects.all().order_by('-id')[:4]
    student_fb = StudentFeedback.objects.last()
    context = {
        'teachers': teachers,
        'student': student_fb
    }
    return render(request, 'index.html', context)


def CreateContact(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            phone_number = request.POST['phone_number']
            email = request.POST['email']
            message = request.POST['message']
            ContactModel.objects.create(
                name = name,
                phone_number = phone_number,
                email = email,
                message = message,
            )
            return redirect('index_url')
        except:
            return redirect('index_url')
 
def about_us(request):
    return render(request, 'about-us.html')


def teachers(request):
    teachers = TeacherModel.objects.all()
    context = {
        'teachers': teachers
    }
    return render(request, 'teachers.html', context)


def contact(request):
    return render(request, 'contact.html')


def vehicle(request):
    return render(request, 'vehicle.html')