# Generated by Django 5.0 on 2024-01-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_published_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='edited_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='published_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
