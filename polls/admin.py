from django.contrib import admin

# Register your models here.
from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):	占据了大量的屏幕区域
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	#fields = ['pub_date', 'question_text']
	fieldsets = [
		(None,				 {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	# 要显示的字段名的元组
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	# 优化Quesiton变更页：过滤器
	list_filter = ['pub_date']
	# 搜索框
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
