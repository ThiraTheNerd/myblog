from django.contrib import admin
from .models import Editor, Post,tags,Comment
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
  filter_horizontal = ('tags',)
admin.site.register(Editor)
admin.site.register(Post, ArticleAdmin)
admin.site.register(tags)