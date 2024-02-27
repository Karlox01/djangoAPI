from django.contrib import admin
from .models import Comment, Image

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'post', 'created_at', 'updated_at', 'content')
    search_fields = ['owner__username', 'post__title', 'content']
    list_filter = ('created_at', 'updated_at', 'owner', 'post')
    actions = ['delete_selected_comments']

    def delete_selected_comments(modeladmin, request, queryset):
        # Delete selected comments and related comment images
        for comment in queryset:
            comment.images.all().delete()
            comment.delete()

    delete_selected_comments.short_description = "Delete selected comments"

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('comment', 'image')
    search_fields = ['comment__content']

    # You can customize this further based on your needs
