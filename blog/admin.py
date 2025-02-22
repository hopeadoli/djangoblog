from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'author')
    fields = ('title', 'text', 'featured_image', 'author', 'published_date')

admin.site.register(Post, PostAdmin)