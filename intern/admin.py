from django.contrib import admin
from .models import Blog
from .models import Document

# class Blog(admin.ModelAdmin):
# 	fieldsets = [
# 		(None, {'fields': ['title','author','publish_time']}),
# 		('Content', {'fields':['content']}),
# 	]

admin.site.register(Blog)
admin.site.register(Document)
# Register your models here.
