# Generated by Django 3.0.8 on 2020-08-14 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0024_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
