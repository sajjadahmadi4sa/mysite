from django.contrib.sitemaps import Sitemap
from blog.models import Post

class Blogsitemap (Sitemap):
    priority = 0.5
    changefreq = 'weekly'
    def items(self):
        return Post.objects.filter(status = 1)
    def lastmod (self,obj):
        return obj.published_date