from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class CommentInLine(admin.StackedInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)