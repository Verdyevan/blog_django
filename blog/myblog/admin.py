from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['id', 'title']

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
