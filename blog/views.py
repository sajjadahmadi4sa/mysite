from django.shortcuts import render , get_object_or_404
from blog.models import Post
from django.utils import timezone

def blog_view(request,pid):
    posts = get_object_or_404(Post , id=pid , published_date__lte = timezone.now())
    posts.counted_view += 1
    posts.save()
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request):
    return render(request,'blog/blog-single.html')

def test (request,pid):
    post = get_object_or_404(Post,pk=pid)
    context = {'post':post}
    return render (request,'test.html',context)

# Create your views here.
