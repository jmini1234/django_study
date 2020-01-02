from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,              {'fields': ['question_text']}),
    ('Date information',{'fields': ['pub_date'],'classes':['collapse']}), #collapse는 숨김
    ] #필드 순서 변경
    inlines = [ChoiceInline] #choice 모델 크래스 같이 보기 

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
