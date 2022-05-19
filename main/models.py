from django.db import models

class TeacherModel(models.Model):
    first_name = models.CharField(max_length=255)
    img = models.ImageField(upload_to = 'teacher')

    def __str__(self):
        return self.first_name

class StudentFeedback(models.Model):
    student = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    body =models.TextField()
    img = models.ImageField(upload_to ='st-fb/')

    def __str__(self):
        return self.student
    
class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name