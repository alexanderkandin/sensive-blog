from django.contrib import admin
from blog.models import Post, Tag, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","author","published_at",)
    raw_id_fields = ('author','tags',)
    exclude = ["likes",]
    readonly_fields = ('published_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('post','author',)
    readonly_fields = ('published_at',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)


