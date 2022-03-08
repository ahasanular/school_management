from django.db import models
from schoolManagement.models import SchoolManagementModel, history_time_info
from django.contrib.auth.models import User
from teachers.models import Teacher
from students.models import Student


class Posts(SchoolManagementModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="postUser")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    post_by = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(max_length=1000, null=True, blank=True)
    img = models.ImageField(null=True, blank=True, upload_to='posts/img')

    def __str__(self):
        return str(self.id)

    # def __str__(self):
    #     return self.user.first_name + "  - [" + self.user.email + "]  - "


class PostLikes(SchoolManagementModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.PROTECT, related_name="post_like")

    def __str__(self):
        return str(self.user) + " - " + str(self.post)

from django.db.models.signals import pre_save

pre_save.connect(history_time_info, sender=Posts)
pre_save.connect(history_time_info, sender=PostLikes)

