# Generated by Django 3.0.6 on 2020-06-18 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_auto_20200613_1812'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['user'], 'verbose_name': 'комметарий ', 'verbose_name_plural': 'комментарии'},
        ),
    ]
