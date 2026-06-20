from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    return render(request,'website/contact.html')
# Create your views here.
