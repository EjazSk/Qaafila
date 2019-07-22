from django.db import models
from django.conf import settings

# Create your models here.
class Darja(models.Model):
  text = models.CharField(max_length=255)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_likes')

  def __str__(self):
    return str(self.text)

  class Meta:
    ordering = ['-created_at']


class Comment(models.Model):
  post = models.ForeignKey(Darja, on_delete=models.CASCADE)
  commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  comment = models.CharField(max_length=140)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str('Comments of '+str(self.post))

  class Meta:
    ordering = ['-created_at']


class hashTag(models.Model):
  tag_name = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.tag_name)