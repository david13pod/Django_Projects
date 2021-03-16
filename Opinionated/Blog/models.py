
from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey('auth.User') # connects each author to an auth user
    published_date=models.DateTimeField(blank=True,null=True)
    title=models.CharField(max_length=200)
    create_date=models.DateTimeField(default=timezone.now())
    text=models.TextField()

    def __str__(self) :
        return self.title

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self): # to return the webpage to list of posts after commenting
        return reverse("Post_detail",kwargs={'pk':self.pk})

class Comment(models.Model):
    post=models.ForeignKey('Blog.Post', related_name='comments') #connects each comment to a post
    author=models.CharField(max_length=100)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    approve_comment=models.BooleanField(default=False)

    def approve(self):
        self.approve_comment=True
        self.save()

    def get_absolute_url(self): # to return the webpage to list of posts after commenting
        return reverse("Post_detail")

    def __str__(self):
        return self.text
