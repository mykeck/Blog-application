from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import cloudinary
import datetime as dt



class Blogs(models.Model):
  blog_title = models.CharField(max_length=150)
  description = models.TextField()
  blog_image = CloudinaryField('image')
  blog_content = models.TextField()
  author = models.ForeignKey(User,on_delete=models.CASCADE)
  published = models.BooleanField()
  created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)
  
  def __str__(self):
    return "{}-{}-{}-{}-{}-{}-{}-{}-{}".format(self.blog_title,self.description,self.blog_image,self.blog_content,self.author,self.published,self.postded_on,self.created_on,self.pk)            
