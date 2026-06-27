from django.shortcuts import render
from django.http import HttpResponse , HttpResponsePermanentRedirect
from blog.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from website.models import Contact
from website.forms import ContactForm , NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = 'unknown'
            contact.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
        else:
            print(form.errors)
            messages.add_message(request,messages.ERROR,'your ticket didnt submited' )
    else:
        form = ContactForm()
    return render(request,'website/contact.html',{'form': form})

def Newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect('/')
    else:
        return HttpResponsePermanentRedirect('/')
    form = NewsletterForm()

def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid(): 
           form.save()
           return HttpResponse ('DONE')
        else:
            return HttpResponse ('not valid')
    form = ContactForm() 
    return render(request,'website/test.html',{'form':form})
# Create your views here.
