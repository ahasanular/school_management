from django.db import models
from schoolManagement.models import SchoolManagementModel

class Footer(SchoolManagementModel):
    addr_street = models.CharField(max_length=75)
    addr_city = models.CharField(max_length=20)
    addr_zip = models.PositiveIntegerField()
    addr_country = models.CharField(max_length=20)
    follow_phone = models.CharField(max_length=20, unique=True)
    follow_email = models.EmailField(unique=True)
    follow_facebook = models.URLField()
    follow_linkedin = models.URLField()
    follow_instagram = models.URLField()
    copyright_name = models.CharField(max_length=70, null=True)
    copyright_year = models.CharField(max_length=4, null=True)
    icon = models.ImageField(null=True, blank=True, upload_to='about/icon')

    def __str__(self):
        return self.addr_street + ", " + self.addr_city+ ", "+ str(self.addr_zip) + ", "+ self.addr_country

from schoolManagement.models import history_time_info
from django.db.models.signals import pre_save, post_save

pre_save.connect(history_time_info, sender=Footer)