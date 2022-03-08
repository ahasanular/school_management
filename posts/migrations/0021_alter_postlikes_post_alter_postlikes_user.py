# Generated by Django 4.0.1 on 2022-02-26 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0020_alter_postlikes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlikes',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='post_like', to='posts.posts'),
        ),
        migrations.AlterField(
            model_name='postlikes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]