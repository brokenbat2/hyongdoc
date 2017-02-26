from django.contrib import admin
from .models import Article
from .models import Comment

class BlogAdmin(admin.ModelAdmin):
    pass
admin.site.register(Article, BlogAdmin)
admin.site.register(Comment, BlogAdmin)
