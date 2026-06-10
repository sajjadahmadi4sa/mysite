from django.db import models
from django.contrib.auth.models import User

class Category (models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Post (models.Model):
    image = models.ImageField(upload_to= 'blogs/',default='blogs/hero-bg.jpg')
    Category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null = True)
    content = models.TextField()
    counted_view = models.IntegerField(default= 0)
    status = models.BooleanField(default= False)
    published_date = models.DateField(null=True)
    created_date = models.DateField(auto_now_add= True)
    updated_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['created_date']
    # def snippets(self):
    #     return self.content[:100] + '...'
    
    def excerpt (self):
        return ' '.join(self.content.split()[:20]) + '...'
    
# Create your models here.
