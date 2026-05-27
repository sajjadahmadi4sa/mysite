from django.urls import path
from website.views import *

urlpatterns = [
    path('',index_view, name= 'Home'),
    path('about/',about_view , name= 'About'),
    path('contact/',contact_view, name= 'Contact'),
    
]
