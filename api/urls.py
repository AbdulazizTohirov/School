from django.urls import path
from .views import*


urlpatterns = [
    # Teacher_urls
    path('teacher/list/', TeacherListView.as_view()),
    path('teacher/create/', TeacherCreateView.as_view()),
    path('teacher/detail/<int:pk>/', TeacherDetialtView.as_view()),

    # Student_urls
    path('student/list/', StudentFeedbackListView.as_view()),
    path('student/create/', StudentFeedbackCreateView.as_view()),
    path('student/detail/<int:pk>/', StudentFeedbackDetailView.as_view()),

    # Contact_urls
    path('contact/list/', ContactListView.as_view()),
    path('contact/create/', ContactCreateView.as_view()),
    path('contact/detail/<int:pk>', ContactDetailView.as_view()),

    # auth
    path('user/crete/', UserCreateView.as_view()),
    path('user/', user_create)
]
