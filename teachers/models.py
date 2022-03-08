from django.db import models
from .string import GENDER_CHOICES, RELIGION_CHOICES, NATIONALITY_DEFAULT, EDU_CHOICES, BLOODGROUP_CHOICES
from schoolManagement.models import SchoolManagementModel
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import secrets

class Teacher(SchoolManagementModel):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=100, null=True, blank=True)
    mothers_name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length= 20, choices=GENDER_CHOICES, null=True, blank=True)
    religion = models.CharField(max_length= 20, choices=RELIGION_CHOICES, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    address = models.TextField(max_length=70, null=True, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOODGROUP_CHOICES, null=True, blank=True)
    nationality = models.CharField(default=NATIONALITY_DEFAULT, max_length=50, null=True, blank=True)
    img = models.ImageField(null=True, blank=True, upload_to='teachers/dp/')
    salary = models.PositiveIntegerField(null=True, blank=True)
    otp = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.full_name)
            teacher_ex = Teacher.objects.filter(slug=slug).exists()
            if teacher_ex:
                hexa = secrets.token_hex(6)
                self.slug = slug + "-Xyb90d-" + hexa
            else:
                self.slug = slug
            super(Teacher, self).save(*args, **kwargs)
        else:
            super(Teacher, self).save(*args, **kwargs)


class TeacherEducation(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name="teacherEducation")
    teacher_edu = models.CharField(max_length=5, choices=EDU_CHOICES)
    speciality = models.CharField(max_length=20)
    passing_year = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return self.teacher.full_name + ' ' + self.teacher_edu + ' ' + str(self.speciality)

class TeacherExperience(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name="teacherExperience")
    exp_name = models.CharField(max_length=50)
    exp_start_date = models.DateField()
    exp_end_date = models.DateField()
    exp_designation = models.CharField(max_length=20)
    speciality = models.CharField(max_length=20)

    def __str__(self):
        return self.teacher.full_name + ' (' + self.speciality + ') [' + self.exp_name + ']'

from django.db.models.signals import pre_save, post_save
from schoolManagement.models import history_time_info

pre_save.connect(history_time_info, sender=Teacher)
pre_save.connect(history_time_info, sender=TeacherEducation)
pre_save.connect(history_time_info, sender=TeacherExperience)
