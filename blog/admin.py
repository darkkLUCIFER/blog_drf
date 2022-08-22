from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent_post', 'author', 'created', 'status',)
    list_editable = ('status',)
    prepopulated_fields = {'slug': ('title',)}
