from django.db import models

# Create your models here.
class jobs(models.Model):
    Image = models.ImageField(upload_to = 'Images/')
    summary = models.CharField(max_length = 200)  
