from django.contrib import admin
from .models import MyImage, ContactSubmission, WriterApplication
from django.utils.html import format_html
from django.urls import reverse


class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "submitted_at", "reviewed")
    list_filter = ("reviewed", "subject", "submitted_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("name", "email", "subject", "message", "submitted_at")
    actions = ["mark_as_reviewed", "mark_as_unreviewed"]

    def mark_as_reviewed(self, request, queryset):
        queryset.update(reviewed=True)

    mark_as_reviewed.short_description = "Mark selected submissions as reviewed"

    def mark_as_unreviewed(self, request, queryset):
        queryset.update(reviewed=False)

    mark_as_unreviewed.short_description = "Mark selected submissions as not reviewed"

    def get_queryset(self, request):
        # Default ordering - newest first
        return super().get_queryset(request).order_by("-submitted_at")


class WriterApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "topic",
        "article_idea",
        "submitted_at",
        "is_reviewed",
    )
    list_filter = ("is_reviewed", "topic", "submitted_at")
    search_fields = ("name", "email", "article_idea", "writing_experience")
    readonly_fields = (
        "name",
        "email",
        "topic",
        "article_idea",
        "writing_experience",
        "writing_samples",
        "submitted_at",
    )
    actions = ["mark_as_reviewed", "mark_as_unreviewed"]

    def mark_as_reviewed(self, request, queryset):
        queryset.update(is_reviewed=True)

    mark_as_reviewed.short_description = "Mark selected submissions as reviewed"

    def mark_as_unreviewed(self, request, queryset):
        queryset.update(is_reviewed=False)

    mark_as_unreviewed.short_description = "Mark selected submissions as not reviewed"

    def get_queryset(self, request):
        # Default ordering - newest first
        return super().get_queryset(request).order_by("-submitted_at")


# Register your models here.
admin.site.register(MyImage)
admin.site.register(ContactSubmission, ContactSubmissionAdmin)
admin.site.register(WriterApplication, WriterApplicationAdmin)
