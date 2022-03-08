from django.db import models
from .strings import GENDER_CHOICES, RELIGION_CHOICES, BLOODGROUP_CHOICES, CLASS_CHOICES, SECTION_CHOICES, NATIONALITY_DEFAULT
from schoolManagement.models import SchoolManagementModel
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import secrets


class Student(SchoolManagementModel):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=50, null=True, blank=True)
    mothers_name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    religion = models.CharField(max_length=10, choices=RELIGION_CHOICES, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    blood_group = models.CharField(null=True, max_length=3, choices=BLOODGROUP_CHOICES)
    nationality = models.CharField(default=NATIONALITY_DEFAULT, max_length=50, null=True, blank=True)
    img = models.ImageField(upload_to='students/dp', null=True)
    otp = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.full_name)
            student_ex = Student.objects.filter(slug=slug).exists()
            if student_ex:
                hexa = secrets.token_hex(6)
                self.slug = slug + "-Xyb90d-" + hexa
            else:
                self.slug = slug
            super(Student, self).save(*args, **kwargs)

        else:
            super(Student, self).save(*args, **kwargs)


class StudentClassInfo(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='studentClassInfo')
    std_class = models.CharField(max_length=2, choices=CLASS_CHOICES)
    roll = models.PositiveIntegerField()
    section = models.CharField(max_length=2, choices=SECTION_CHOICES)
    admission_date = models.DateField()

    def __str__(self):
        return self.student.full_name + ' ' + self.std_class + ' ' + str(self.roll)


from django.db.models.signals import pre_save, post_save
from schoolManagement.models import history_time_info

pre_save.connect(history_time_info, sender=Student)
pre_save.connect(history_time_info, sender=StudentClassInfo)