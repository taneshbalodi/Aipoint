# Generated by Django 2.2.5 on 2020-04-26 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0016_auto_20200426_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
