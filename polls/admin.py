from django.contrib import admin
from .models import Choice, Question

# 이렇게 할수도 있고,
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # admin list 에서 field 들 순서를 고를 수 있음
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # 이거 있으면 옆에 필터 사이드 바가 생김. DateTimeField 여서 적절한 필터 옵션을 제공함
    list_filter = ['pub_date']

    # 이거 있으면 위에 검색창이 생김. question_text에 LIKE 쿼리를 사용함
    search_fields = ['question_text']

    # admin detail 에서 field 들에 대해 더 이쁘게 볼 수 있음
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
# Choice를 관리할 수 있게 하자
admin.site.register(Choice)
