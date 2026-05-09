from django.conf import Settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
  
  class Status(models.TextChoices): #enumaration class
    DRAFT = 'DF', 'Draft'
    PUBLISHED = 'PB', 'Published'
    
  title = models.CharField(max_length=250)
  slug = models.SlugField(max_length=250)
  body = models.TextField()
  #autho many to one rel
  author = models.ForeignKey(
    Settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='blog_posts'
  )
  
  publish = models.DateTimeField(default=timezone.now)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  
  status = models.CharField(
    max_length=2,
    choices=Status,
    default=Status.DRAFT
  )
  
  class Meta:
    ordering = ['-publish']  
    #index 
    indexes = [
      models.Index(fields=['-publish']),
    ]
    
  def __str__(self):
    return self.title

