from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from movie.models import Movies
from django.urls import reverse

class comment(models.Model):
    comment_title = models.CharField(max_length=255)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_commented = models.ForeignKey(Movies, on_delete=models.CASCADE,null=True)

    def __str__(self): # how we want it to print out
        return self.comment_title

    def get_absolute_url(self):
        return reverse('comment_detail',kwargs={'pk':self.pk})
