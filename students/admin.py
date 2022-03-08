from django.contrib import admin
from .models import Student, StudentClassInfo

class StudentAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = Student.objects.filter(is_archived=False).all().order_by('id')
        return queryset

    search_fields = ['full_name__icontains']

    fields = [
        'user',
        ('full_name', 'slug'),
        ('fathers_name', 'mothers_name'),
        ('gender', 'religion', 'birth_date'),
        ('email', 'phone'),
        'address',
        ('img', 'blood_group'),
        ('is_archived', 'otp'),
    ]

    readonly_fields = ['slug']

    list_display = ['id', 'otp', 'full_name', 'email', 'phone', 'created_at', 'modified_at', 'is_archived', 'archived_at']
    list_per_page = 30


admin.site.register(Student, StudentAdmin)

class StudentClassInfoAdmin(admin.ModelAdmin):

    fields = ['student', 'std_class', 'roll', 'section', 'admission_date']
    list_display = ['student', 'std_class', 'roll', 'section', 'admission_date']

admin.site.register(StudentClassInfo, StudentClassInfoAdmin)


