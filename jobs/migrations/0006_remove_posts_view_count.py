# Generated by Django 2.2.5 on 2020-04-16 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20200416_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='view_count',
        ),
    ]