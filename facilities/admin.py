from django.contrib import admin
from .models import Facility

class FacilityAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = Facility.objects.filter().all().order_by('id')
        return queryset
    fields = ['name', 'details', 'img']

    list_per_page = 3

admin.site.register(Facility, FacilityAdmin)