# Generated by Django 3.0.6 on 2020-06-12 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20200611_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='author_photo'),
        ),
    ]