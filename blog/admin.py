from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title","author","published_at",)
    raw_id_fields = ('author','tags',)
    exclude = ["likes",]
    readonly_fields = ('published_at',)


class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('post','author',)
    readonly_fields = ('published_at',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Post,PostAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Comment,CommentAdmin)
