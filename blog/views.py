from django.shortcuts import render , get_object_or_404
from blog.models import Post
from django.utils import timezone

def blog_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(),status = 1)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request, pid):
    posts = get_object_or_404(Post,id=pid,status=True)
    next_post = Post.objects.filter(id__gt = posts.id,status=True).order_by('id').first()
    previous_post = Post.objects.filter(id__lt = posts.id,status=True).order_by('-id').first()
    posts.counted_view += 1
    posts.save()
    context = {'posts': posts , 'next_post':next_post , 'previous_post':previous_post}
    return render(request,'blog/blog-single.html',context)

#def test (request,pid):
    post = get_object_or_404(Post,pk=pid)
    context = {'post':post}
    return render (request,'test.html',context)

# Create your views here.
