# Generated by Django 3.2.13 on 2022-05-27 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_title_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title_tag',
        ),
    ]
