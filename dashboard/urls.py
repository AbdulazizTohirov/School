from django.urls import path
from .views import *
urlpatterns = [
    path('', index_view, name='dashboard_url'),
    path('teachers/', teachers, name='teacher_url'),
    path('teacher/create/', teacher_create, name='teacher_create_url'),
    path('students/', student_feedback, name='students_url'),
    path('student/create/', student_create, name='create_student_url'),
    path('requests/', requests, name='requests_url'),

# account
    path('register/', register_view, name='register_url'),
    path('login/', login_view, name='login_url'),
    path('logout/', logout_view, name='logout_url'),
]