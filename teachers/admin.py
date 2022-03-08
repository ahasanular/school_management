from django.contrib import admin
from .models import Teacher, TeacherEducation, TeacherExperience

class TeacherAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        query_set = Teacher.objects.filter(is_archived=False).all().order_by('id')
        return query_set

    search_fields = ['full_name__icontains']

    fields = [
        ('user', 'full_name', 'slug' , 'fathers_name'),
        ('gender', 'religion', 'birth_date'),
        ('email', 'phone'),
        'address',
        'img',
        ('blood_group', 'nationality'),
        'salary',
        ('is_archived', 'otp'),
    ]

    readonly_fields = ['slug']

    list_display = ['id', 'otp', 'full_name', 'email', 'phone', 'created_at', 'modified_at', 'is_archived', 'archived_at']
    list_per_page = 30


admin.site.register(Teacher, TeacherAdmin)


class TeacherEducationAdmin(admin.ModelAdmin):
    pass

admin.site.register(TeacherEducation, TeacherEducationAdmin)

class TeacherExperienceAdmin(admin.ModelAdmin):
    pass

admin.site.register(TeacherExperience, TeacherExperienceAdmin)