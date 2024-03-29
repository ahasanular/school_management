# Generated by Django 4.0.1 on 2022-02-03 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(max_length=255, null=True)),
                ('created_from', models.CharField(max_length=255, null=True)),
                ('modified_by', models.CharField(max_length=255, null=True)),
                ('modified_at', models.DateTimeField(max_length=255, null=True)),
                ('modified_from', models.CharField(max_length=255, null=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('archived_by', models.CharField(max_length=255, null=True)),
                ('archived_at', models.DateTimeField(max_length=255, null=True)),
                ('archived_from', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=50)),
                ('Description', models.TextField(max_length=255)),
                ('img', models.ImageField(upload_to='facilities/pics')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
