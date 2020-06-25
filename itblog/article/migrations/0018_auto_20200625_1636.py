# Generated by Django 3.0.6 on 2020-06-25 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_auto_20200618_2050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'статья', 'verbose_name_plural': 'статьи'},
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'автор', 'verbose_name_plural': 'авторы'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'тег', 'verbose_name_plural': 'теги'},
        ),
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='articles/20200625'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='article.Article'),
        ),
    ]
