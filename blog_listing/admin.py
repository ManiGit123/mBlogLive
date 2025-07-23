from django.contrib import admin
from .models import MyImage, ContactSubmission, WriterApplication, NewsletterSubscriber
from django.utils.html import format_html
from django.urls import reverse
from django.urls import path
from django.shortcuts import get_object_or_404, redirect


class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "message", "submitted_at", "reviewed_status")
    list_filter = ("reviewed", "subject", "submitted_at")
    list_filter_horizontal = ("reviewed", "subject", "submitted_at")
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

    def reviewed_status(self, obj):
        url = reverse("blog_listing:toggle_reviewed", args=[obj.pk])
        if obj.reviewed:
            return format_html('<a href="{}" style="color: green;">✓ Reviewed</a>', url)
        return format_html('<a href="{}" style="color: red;">✗ Not Reviewed</a>', url)

    reviewed_status.short_description = "Status"
    reviewed_status.allow_tags = True

    def changelist_view(self, request, extra_context=None):
        # Add any extra context if needed
        extra_context = extra_context or {}
        extra_context["title"] = "Custom Title"  # Optional
        return super().changelist_view(request, extra_context=extra_context)

    class Media:
        css = {"all": ("css/admin-custom.css",)}


class ReviewedFilter(admin.SimpleListFilter):
    title = "review status"
    parameter_name = "is_reviewed"

    def lookups(self, request, model_admin):
        return (
            ("reviewed", "Reviewed"),
            ("unreviewed", "Unreviewed"),
        )

    def queryset(self, request, queryset):
        if self.value() == "reviewed":
            return queryset.filter(is_reviewed=True)
        if self.value() == "unreviewed":
            return queryset.filter(is_reviewed=False)


class WriterApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "topic", "article_idea", "submitted_at", "is_reviewed")
    list_filter = (ReviewedFilter, "topic", "submitted_at")
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

    def changelist_view(self, request, extra_context=None):
        # Add any extra context if needed
        extra_context = extra_context or {}
        extra_context["title"] = "Custom Title"  # Optional
        return super().changelist_view(request, extra_context=extra_context)

    class Media:
        css = {"all": ("css/admin-custom.css",)}


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at", "is_active", "source")
    list_filter = ("source", "subscribed_at", "is_active")
    search_fields = ("email", "source")
    readonly_fields = ("email", "subscribed_at", "is_active", "source")
    # actions = ["mark_as_reviewed", "mark_as_unreviewed"]

    # def mark_as_reviewed(self, request, queryset):
    #     queryset.update(is_reviewed=True)

    # mark_as_reviewed.short_description = "Mark selected submissions as reviewed"

    # def mark_as_unreviewed(self, request, queryset):
    #     queryset.update(is_reviewed=False)

    # mark_as_unreviewed.short_description = "Mark selected submissions as not reviewed"

    def get_queryset(self, request):
        # Default ordering - newest first
        return super().get_queryset(request).order_by("-subscribed_at")


# Register your models here.
admin.site.register(MyImage)
admin.site.register(ContactSubmission, ContactSubmissionAdmin)
admin.site.register(WriterApplication, WriterApplicationAdmin)
admin.site.register(NewsletterSubscriber, SubscriberAdmin)
