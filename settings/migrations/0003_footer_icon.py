# Generated by Django 4.0.1 on 2022-02-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_footer_copyright_name_footer_copyright_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='about/icon'),
        ),
    ]