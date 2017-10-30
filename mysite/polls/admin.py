from django.contrib import admin
from .models import *


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    #  fields = ['question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('MyField', {'fields': ['pub_date']}),
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
