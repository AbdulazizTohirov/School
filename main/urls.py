from django.urls import path
from .views import *
urlpatterns = [
    path('', index_view, name='index_url'),
    path('teachers/', teachers, name='teachers_url'),
    path('about/us/', about_us, name='about_us_url'),
    path('contact/', contact, name='contact_url'),
    path('vehicle/', vehicle, name='vehicle_url'),
    path('contact/create/', CreateContact, name='create_url')
]