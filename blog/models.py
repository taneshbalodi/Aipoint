from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class blog(models.Model):
    Title = models.CharField(max_length=260)
    Publ_date = models.DateTimeField()
    Body = RichTextUploadingField()
    image = models.ImageField(upload_to="images/")


    def __str__(self):
        return self.Title

    def summary(self):
        return self.Body[:70]
