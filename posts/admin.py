from django.contrib import admin
from .models import Posts, PostLikes

class PostsAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        query_set = Posts.objects.filter(is_archived=False).all().order_by('id')
        return query_set

    fields = ['user', 'post_by', 'text', 'img', 'is_archived']
    list_display = ['id', 'user', 'is_archived', 'created_at', 'modified_at', 'archived_at']

admin.site.register(Posts, PostsAdmin)

class PostLikesAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        query_set = PostLikes.objects.filter(is_archived=False).all().order_by('id')
        return query_set

    fields = ['user', 'post']
    list_display = ['user', 'post', 'is_archived', 'created_at']

admin.site.register(PostLikes, PostLikesAdmin)