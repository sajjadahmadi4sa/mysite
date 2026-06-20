from django import template
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
register = template.Library()

@register.inclusion_tag('website/latest_posts.html',takes_context=True)
def latestposts(context):
    request = context['request']
    posts = Post.objects.filter(published_date__lte=timezone.now(),status=1).order_by('-published_date')[:6]
    posts = Paginator(posts,3)
    
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts':posts}
    return{'posts':posts}