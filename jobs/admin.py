from django.contrib import admin

from django.db import models

# Register your models here.
from .models import  Author , category, posts , Comment

admin.site.register(Author)
admin.site.register(category)
admin.site.register(posts)
admin.site.register(Comment)
