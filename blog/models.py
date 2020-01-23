from django.db import models

# Create your models here.
class blog(models.Model):
    Title = models.CharField(max_length=260)
    Publ_date = models.DateTimeField()
    Body = models.TextField()
    image = models.ImageField(upload_to="images/")
