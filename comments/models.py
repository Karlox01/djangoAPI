from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Image(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    images = models.ManyToManyField(Image, related_name='comments', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
