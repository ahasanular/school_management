# Generated by Django 4.0.1 on 2022-02-26 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_postlikes_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postlikes',
            name='likes',
        ),
        migrations.AlterField(
            model_name='posts',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]