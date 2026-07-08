from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class LatestPostsFeed(Feed):
    title = "Blog Newest Posts"
    link = "/rss/feed"
    description = "Latest posts from my blog"

    def items(self):
        return Post.objects.filter(status=True).order_by("-published_date")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]

    def item_link(self, item):
        return reverse("blog:single", args=[item.id])