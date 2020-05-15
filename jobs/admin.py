from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
from .models import  Author , category, posts , Comment

admin.site.register(Author)
admin.site.register(category)
admin.site.register(posts)
admin.site.register(Comment)



formfield_overrides = {
models.TextField: {'widget': TinyMCE()},
}
