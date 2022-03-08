# Generated by Django 4.0.1 on 2022-02-09 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0006_teacher_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='fathers_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='religion',
            field=models.CharField(blank=True, choices=[('Muslim', 'Muslim'), ('Christian', 'Christan')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='salary',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]