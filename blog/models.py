from django.db import models
from datetime import datetime
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def get_absolute_url(self):
        return reverse('blog:blog-index')

    def __str__(self):
        return self.title

