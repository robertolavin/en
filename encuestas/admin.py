# admin.py
from django.contrib import admin
from .models import Survey, Question  # Eliminar SurveyDetail si no se va a utilizar

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'survey', 'question_type')
    list_filter = ('survey', 'question_type')
    search_fields = ('text',)


