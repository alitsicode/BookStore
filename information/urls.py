from django.urls import path
from . import views

urlpatterns = [
    path('aboutus/',views.aboutus,name='about_us'),
    path('contactus/',views.ContactUs.as_view(),name='contact_us')
]