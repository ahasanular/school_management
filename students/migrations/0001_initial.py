# Generated by Django 4.0.1 on 2022-01-31 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('fathers_name', models.CharField(max_length=50)),
                ('mothers_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('religion', models.CharField(choices=[('Muslim', 'Muslim'), ('Christian', 'Christian'), ('Jewish', 'Jewish'), ('Hindu', 'Hindu')], max_length=10)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('address', models.CharField(max_length=120)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=3)),
                ('img', models.ImageField(upload_to='students/dp')),
            ],
        ),
    ]
