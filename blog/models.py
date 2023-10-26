from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.
'''
    - fields , options 
    - validation
    - html widget

'''
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=30000)
    create_date = models.DateTimeField(default=timezone.now)
    draft = models.BooleanField(default=True)
    tags = TaggableManager()
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='post_user')
    image = models.ImageField(upload_to='posts')
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_author')
    post = models.ForeignKey(Post,related_name='comment_post',on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    create_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.user)