from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from ckeditor.fields import RichTextField


User = get_user_model()



class Author(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE , blank=True)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username



class category(models.Model):
    title = models.CharField(max_length=20)


    def __str__(self):
        return self.title






class posts(models.Model):
    title = models.CharField(max_length=100,blank=True)
    overview = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    content = RichTextField(default=True)

    author = models.ForeignKey(Author, blank=True, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="images/", blank=True )
    categories = models.ManyToManyField(category)
    featured = models.BooleanField()
    previous_post = models.ForeignKey('self', related_name = 'previous' ,on_delete = models.SET_NULL, blank = True, null = True)
    next_post = models.ForeignKey('self', related_name = 'next' , on_delete = models.SET_NULL, blank = True, null = True)



    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs ={
        'id': self.id
        })


    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE , blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    content = models.TextField(blank = True, null=True)
    post = models.ForeignKey(posts, related_name = 'comments' ,on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.user.username
