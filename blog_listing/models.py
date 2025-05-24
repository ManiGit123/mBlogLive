from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from home import blocks
from home.models import FinancialBLog, TravelBLog, TutorialsBLog
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from django.db import models

# Create your models here.


class FinancialBlogListingPage(Page):
    # getting all the blogdetailpages and putting them into then context of this template
    # listing page lists all blog details pages

    template = "financial/fin_blog_listing_page.html"

    custom_title = models.CharField(
        max_length=100, blank=False, null=False, help_text="Overwrite the default title"
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        # Adding custom stuff to our contaxt
        contaxt = super().get_context(request, *args, **kwargs)
        contaxt["posts"] = FinancialBLog.objects.live().public()
        return contaxt


class TravelBlogListingPage(Page):
    # getting all the blogdetailpages and putting them into then context of this template
    # listing page lists all blog details pages

    template = "travel/travel_blog_listing_page.html"

    custom_title = models.CharField(
        max_length=100, blank=False, null=False, help_text="Overwrite the default title"
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        # Adding custom stuff to our contaxt
        contaxt = super().get_context(request, *args, **kwargs)
        contaxt["posts"] = TravelBLog.objects.live().public()
        return contaxt


class TutorailsBlogListingPage(Page):
    # getting all the blogdetailpages and putting them into then context of this template
    # listing page lists all blog details pages

    template = "tutorial/tuto_blog_listing_page.html"

    custom_title = models.CharField(
        max_length=100, blank=False, null=False, help_text="Overwrite the default title"
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        # Adding custom stuff to our contaxt
        contaxt = super().get_context(request, *args, **kwargs)
        contaxt["posts"] = TutorialsBLog.objects.live().public()
        return contaxt


class MyImage(models.Model):
    image = models.ImageField()
