from django.contrib import admin

from polls_app import models

# Register your models here.
@admin.register(models.QuestionModel)
class QuestionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the PostModel.

    This class registers PostModel in the Django admin interface with all its features.

    Attributes:
        date_hierarchy (str): Enables date-based navigation by the specified date field.
        list_display (list[str]): Fields to display as columns in the list view.
        list_filter (list[str]): Fields to filter by in the sidebar.
        search_fields (list[str]): Fields that are searchable in the admin.
        readonly_fields (list[str]): Fields set as read-only in the admin form.
    """

    date_hierarchy = "created_at"
    list_display = ['question_text', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['question_text']
    readonly_fields = ['slug']
