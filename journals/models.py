from django.db import models
from django.db.models.deletion import CASCADE
from tinymce.models import HTMLField
# Create your models here.
class Editor(models.Model):
  username = models.CharField(max_length=30)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField()
  profile_pic = models.ImageField(upload_to = 'profile_pics/')

  def __str__(self):
      return self.first_name
  class Meta:
    ordering = ['first_name']
class tags(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
      return self.name

class Post(models.Model):
  image = models.ImageField(upload_to = 'post_pics/')
  title = models.CharField(max_length=100)
  content = HTMLField()
  editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
  tags = models.ManyToManyField(tags)
  pub_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.title

