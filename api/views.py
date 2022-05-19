from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from main.models import *
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Teachers
class TeacherCreateView(generics.CreateAPIView):
    """This view is Creating Teacher model"""
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAdminUser]


class TeacherListView(generics.ListAPIView):
    """This View is Teachers List"""
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAdminUser]

class TeacherDetialtView(generics.RetrieveUpdateDestroyAPIView):
    """This View is Destroy,Update,Retrive Teachers"""
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# StudentFeedBack

class StudentFeedbackListView(generics.ListAPIView):
    """This view is Creating StudentFeedBack model"""
    queryset = StudentFeedback.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAdminUser]

class StudentFeedbackCreateView(generics.CreateAPIView):
    """This View is StudentFeedBack List"""
    queryset = StudentFeedback.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAdminUser]

class StudentFeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
    """This View is Destroy,Update,Retrive StudentFeedBack"""
    queryset = StudentFeedback.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# ContactModel

class ContactListView(generics.ListAPIView):
    """This view is Creating ContactModel"""
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAdminUser]

class ContactCreateView(generics.CreateAPIView):
    """This View is ContactModel List"""
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAdminUser]

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    """This View is Destroy,Update,Retrive ContactModel"""
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET', 'POST'])
def user_create(request):
    users = User.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        news_user = User.objects.create_user(
            username=username,
            password = password,
            email = email
        )
        
        user = UserSerializer(news_user)
        return Response(user.data, status=status.HTTP_201_CREATED)
    else:
        users_json = UserSerializer(users, many=True)
        return Response(users_json.data, status=status.HTTP_200_OK)