# Generated by Django 2.2.5 on 2020-04-16 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_posts_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='view_count',
            field=models.IntegerField(default=2),
        ),
    ]
