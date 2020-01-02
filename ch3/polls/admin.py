from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
    ('Question Statement',{'fields': ['question_text']}),
    ('Date information',{'fields': ['pub_date'],'classes':['collapse']}), #collapse는 숨김 
    ] #필드 순서 변경

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
