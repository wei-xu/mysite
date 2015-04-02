from django.contrib import admin
from .models import Blog

# class Blog(admin.ModelAdmin):
# 	fieldsets = [
# 		(None, {'fields': ['title','author','publish_time']}),
# 		('Content', {'fields':['content']}),
# 	]

admin.site.register(Blog)
# Register your models here.
