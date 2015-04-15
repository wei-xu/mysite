from django.contrib import admin
from polls.models import Question, Choice, Person, Group, Membership
# Register your models here.

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']
#	date_hierarchy = 'pub_date'
#	fields = [ 'pub_date', 'question_text']

class MemberInline(admin.TabularInline):
	"""docstring for GroupInline"""
	model = Membership
		
class PersonAdmin(admin.ModelAdmin):
	fieldsets = [
		('Person Name', {'fields': ['name']}),
	]
	inlines = [MemberInline]

class GroupAdmin(admin.ModelAdmin):
	"""docstring for Group"""
	fieldsets = [
		('Group Name', {'fields': ['name']}),
	]
	inlines = [MemberInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)