from django.contrib import admin

from polls_app import models

# Register your models here.
@admin.register(models.QuestionModel)
class QuestionAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ['question_text', 'status', 'created_at']
    search_fields = ['question_text']
    list_filter = ['status']
