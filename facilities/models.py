from django.db import models
from schoolManagement.models import SchoolManagementModel

class Facility(SchoolManagementModel):
    name = models.CharField(max_length=50)
    details = models.TextField(max_length=255)
    img = models.ImageField(upload_to='facilities/pics')

    def __str__(self):
        return str(self.id) + self.name
