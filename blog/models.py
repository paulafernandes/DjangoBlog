from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # function to get the url that is going to be used
    # to set the file it should return after insert
    # new post 
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
        # reverse function returns a string with the url
        # returns to detail page, since it demands a pk value
        # sets pk to self.pk

