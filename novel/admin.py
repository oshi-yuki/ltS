from django.contrib import admin
from .models import Tag, Category, Story, Comment
# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Story)
admin.site.register(Comment)
