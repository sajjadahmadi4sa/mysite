from django.contrib import admin
from blog.models import Post , Category,Comment
admin.site.register(Category)
from django_summernote.admin import SummernoteModelAdmin


#admin.site.register(Post,PostAdmin)


class CommentAdmin (admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '_empty_'
    list_display = ('name','post','approved','created_date')
    list_filter = ('post','approved')
    search_fields = ['name','post']
    
@admin.register(Post)
class PostAdmin (SummernoteModelAdmin):
    date_hierarchy = 'published_date'
    empty_value_display = '_empty_'
    list_display = ('title','author','published_date','created_date','updated_date','status','counted_view')
    list_filter = ('status','author')
    search_fields = ['title','content']
    summernote_fields = ('content',)
    
admin.site.register(Comment,CommentAdmin)

    
# Register your models here.