from django.contrib import admin
from .models import *


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    #  fields = ['question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('MyField', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['question_text', 'pub_date']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
