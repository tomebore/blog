# Generated by Django 3.0.6 on 2020-06-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_auto_20200618_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='dislokes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='articles/20200618'),
        ),
        migrations.AddField(
            model_name='article',
            name='reposts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='article', to='article.Tag'),
        ),
    ]