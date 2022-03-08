# Generated by Django 4.0.1 on 2022-02-02 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_teacher_archived_at_teacher_archived_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=3, null=True),
        ),
    ]