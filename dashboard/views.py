from http.client import HTTPResponse
from django.shortcuts import redirect, render
from main.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# index_view
@login_required(login_url='login_url')
def index_view(request):
    teachers_quantity = TeacherModel.objects.all().count()
    requests_quantity = ContactModel.objects.all() .count()
    users_quantity = User.objects.all() .count()
    student_feedback_quantity = StudentFeedback.objects.all() .count()
    requests = ContactModel.objects.all()
    context = {
    'teachers_quantity':teachers_quantity,
    'requests_quantity':requests_quantity,
    'users_quantity': users_quantity,
    'student_feedback_quantity': student_feedback_quantity,
    'requests': requests
    }
    return render(request, 'dashboard/index.html', context)


# teacher_create
@login_required(login_url='login_url')
def teacher_create(request):
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            img = request.FILES['img']
            TeacherModel.objects.create(

            first_name = first_name,
            img = img,
        )
        except:
            return HttpResponse('Xatolik')
        
    return redirect('teachers_url')


# teachers
@login_required(login_url='login_url')
def teachers(request):
    teachers = TeacherModel.objects.all()
    context = {
        'teachers': teachers
    }
    return render(request, 'dashboard/teachers.html', context)


# StudentFeedBack
@login_required(login_url='login_url')
def student_feedback(request):
    students = StudentFeedback.objects.all()
    context = {
        'students':students
    }
    return render(request, 'dashboard/students.html', context)


# Studen_Create
@login_required(login_url='login_url')
def student_create(request):
    if request.method == 'POST':
        try:
            student = request.POST['first_name']
            status = request.POST['status']
            body = request.POST['body']
            img = request.FILES['img']

            StudentFeedback.objects.create(
                student=student,
                status=status,
                body=body,
                img=img
            )
        except:
            return HTTPResponse('XATOLIK')

    return redirect('students_url')


# Requests
@login_required(login_url='login_url')
def requests(request):
    requests = ContactModel.objects.all()
    context = {
        'requests':requests
    }
    return render(request, 'dashboard/requests.html', context)




# ACCOUNT
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_2 = request.POST['password_2']
        if password ==  password_2:
            User.objects.create_user(
                username=username,
                password=password
            )
            
        user = authenticate(username=username, password=password)
        login(request,user)
        return redirect('dashboard_url')
    else:
        return render(request, 'account/register.html')


# Login_View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard_url')
            else:
                return HttpResponse(False)
        return HttpResponse(False)
    return render(request, 'account/login.html')

# Logout_View
def logout_view(request):
    return redirect('index_url')
# forregin key
# many to many
# one to one