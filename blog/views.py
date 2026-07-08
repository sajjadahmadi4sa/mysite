from django.shortcuts import render , get_object_or_404
from blog.models import Post , Comment
from django.utils import timezone
from django.core.paginator import Paginator , PageNotAnInteger,EmptyPage
from django.http import HttpResponse
from blog.forms import CommentForm
from django.contrib import messages
def blog_view(request , cat_name=None , author_username=None , tag_name=None):
    posts = Post.objects.filter(published_date__lte=timezone.now(),status = 1)
    if cat_name:
        posts = posts.filter(Category__name = cat_name)
    if author_username:
        posts = posts.filter(author__username = author_username)
    if tag_name :
        posts = posts.filter(tag__name__in=['tag_name'])
    posts = Paginator(posts,3)  
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger :
        posts = posts.get_page(1)
    except EmptyPage :
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.add_message(request,messages.SUCCESS,'comment submit succesfuly')
        else:
            messages.add_message(request,messages.ERROR,'comment is not submited ')
    posts = get_object_or_404(Post,id=pid,status=True)
    form = CommentForm()
    next_post = Post.objects.filter(id__gt = posts.id,status=True).order_by('id').first()
    previous_post = Post.objects.filter(id__lt = posts.id,status=True).order_by('-id').first()
    posts.counted_view += 1
    posts.save()
    comments = Comment.objects.filter(post=posts.id,approved=True).order_by('-created_date')
    print(comments)
    print(comments.count())
    context = {'posts': posts , 'next_post':next_post , 'previous_post':previous_post , 'comments':comments,'form':form}
    return render(request,'blog/blog-single.html',context)

def test(request):
    posts = Post.objects.filter(status = 1)
    context = {'posts':posts}
    return render (request,'test.html',context)

def blog_category(request,cat_name):
    posts = Post.objects.filter(published_date__lte=timezone.now(),status = 1)
    posts = posts.filter(Category__name = cat_name)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def blog_search(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(),status = 1) 
    if request.method == 'GET':
        posts = posts.filter(content__icontains=request.GET.get('s'))
        context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

# Create your views here.
