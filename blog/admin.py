from django.contrib import admin
from blog.models import Post
#admin.site.register(Post,PostAdmin)
@admin.register(Post)
class PostAdmin (admin.ModelAdmin):
    date_hierarchy = 'published_date'
    empty_value_dislay = '_empty_'
    list_display = ('title','author','published_date','created_date','updated_date','status','counted_view')
    list_filter = ('status','author')
    search_fields = ['title','content']
    
    
    
# Register your models here.
