from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from .helpers import *
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
import tinymce
from django.urls import reverse


# Create your models here.

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Profile = models.ImageField(default='default.png')

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class BlogModel(models.Model):
    title=models.CharField(max_length=1000)
    content = HTMLField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to="media",default="/static/img/post1.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    category = models.ManyToManyField(Category)
    featured = models.BooleanField(default=False)
    # view_count = models.IntegerField(default=0)
    # comment_count = models.IntegerField(default=0)
    previous_post = models.ForeignKey('self',related_name='previous',on_delete=models.SET_NULL,blank=True,null=True)
    next_post = models.ForeignKey('self',related_name='next',on_delete=models.SET_NULL,blank=True,null=True)
    

    


    
    def __srt__(self):
        return self.title + '|' + str(self.author)

    def snipet(self):
        return self.content[:10]

    def recent(self):
        return self.content[:30]

    def aside(self):
        return self.content[:195]




    def save(self,*args,**kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel,self).save(*args,**kwargs)
    

    def get_absolute_url(self):
        return reverse('blog_details', kwargs={
            'pk': self.pk
        })

    def get_update_url(self):
        return reverse('post-update',kwards={
            'id':self.id
        })

    def get_delete_url(self):
        return reverse('post-delete',kwards={
            'id':self.id
        })

    @property
    def get_comments(self):
        return self.comments.all()
    
    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey('BlogModel',related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



class PostView(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey('BlogModel', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    