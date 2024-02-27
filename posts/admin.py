from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #  existing Profile admin configurations

    def user_posts(self, obj):
        return "\n".join([str(post) for post in obj.owner.posts.all()])

    user_posts.short_description = "User Posts"

# Import the Post and PostImage models
from .models import Post, PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'title', 'created_at', 'updated_at')
    search_fields = ['owner__username', 'title', 'content']
    list_filter = ('created_at', 'updated_at', 'owner')
    actions = ['delete_selected_posts']

    def delete_selected_posts(modeladmin, request, queryset):
        # Delete selected posts and related post images
        for post in queryset:
            post.images.all().delete()
            post.delete()

    delete_selected_posts.short_description = "Delete selected posts"

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')
    search_fields = ['post__title']


