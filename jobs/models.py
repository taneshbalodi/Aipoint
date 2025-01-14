from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.http import HttpResponse
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from jobs.utils import unique_slug_generator




User = get_user_model()



class Author(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE , blank=True)
    profile_picture = models.ImageField()
    Desc = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username

    def __str__(self):
        return self.Desc



class category(models.Model):
    title = models.CharField(max_length=20)
    Image = models.ImageField()
    Description = models.CharField(max_length=100,blank=True)


    def __str__(self):
        return self.title


    @staticmethod
    def get_all_categories():
        return Category.obects.all()








class posts(models.Model):
    title = models.CharField(max_length=100,blank=True)
    overview = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    content = RichTextField(default=True)
    slug = models.SlugField(max_length = 250, null = True, blank = True)

    author = models.ForeignKey(Author, blank=True, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="images/", blank=True )
    categories = models.ManyToManyField(category)
    featured = models.BooleanField()
    previous_post = models.ForeignKey('self', related_name = 'previous' ,on_delete = models.SET_NULL, blank = True, null = True)
    next_post = models.ForeignKey('self', related_name = 'next' , on_delete = models.SET_NULL, blank = True, null = True)


    @staticmethod
    def get_all_categories_id(category_title):
        return posts.obects.filter(category = category_title)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs ={
        'slug': self.slug
        })

def slug_generator(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=posts)





class Comment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE , blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    content = models.TextField(blank = True, null=True)
    post = models.ForeignKey(posts, related_name = 'comments' ,on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.user.username
