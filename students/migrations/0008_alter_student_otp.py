# Generated by Django 4.0.1 on 2022-02-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_student_otp_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='otp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]