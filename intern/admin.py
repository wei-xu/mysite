from django.contrib import admin
from .models import Blog, Wiki, WikiEditHistory
from .models import Document

# class Blog(admin.ModelAdmin):
# 	fieldsets = [
# 		(None, {'fields': ['title','author','publish_time']}),
# 		('Content', {'fields':['content']}),
# 	]
class WikiEditHistoryInline(admin.TabularInline):
	model = WikiEditHistory
	extra = 1

class WikiAdmin(admin.ModelAdmin):
	inlines = [WikiEditHistoryInline]

admin.site.register(Blog)
admin.site.register(Document)
admin.site.register(Wiki, WikiAdmin)
# Register your models here.
