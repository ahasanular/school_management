# Generated by Django 4.0.1 on 2022-02-22 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0012_alter_teacher_otp'),
        ('students', '0011_alter_student_otp'),
        ('posts', '0005_posts_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='user',
        ),
        migrations.AddField(
            model_name='posts',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='students.student'),
        ),
        migrations.AddField(
            model_name='posts',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='teachers.teacher'),
        ),
    ]
