from django.contrib import admin
from .models import Footer

class FooterAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = Footer.objects.filter().all().order_by('id')
        return queryset

    fields = [
        'icon',
        'addr_street',
        ('addr_city', 'addr_zip', 'addr_country'),
        ('follow_phone', 'follow_email'),
        ('follow_facebook', 'follow_linkedin', 'follow_instagram'),
        ('copyright_name', 'copyright_year'),
        'is_archived',
    ]

    list_display = ['id', 'addr_street', 'addr_city', 'addr_zip', 'addr_country', 'follow_phone', 'follow_email', 'follow_facebook', 'follow_linkedin' , 'follow_instagram', 'is_archived', 'created_at', 'modified_at', 'archived_at']

admin.site.register(Footer, FooterAdmin)