from django.db import models

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from . import blocks
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel

# from modelcluster.fields import ParentalKey


class HomePage(Page):
    template = "home/home_page.html"
    # max_count = 1  # restrict child
    banner_title = models.CharField(max_length=300, blank=False, null=True)
    banner_subtitle = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
    ]


class FinancialBLog(Page):
    template = "financial/financial_page.html"
    fin_title = models.CharField(max_length=300, blank=False, null=True)
    fin_subtitle = RichTextField(blank=True)
    content = StreamField(
        [
            ("title_and_text", blocks.TitleandTexBlock()),
            ("rich_text", blocks.RichTextBlock()),
            ("simple_rich_text", blocks.SimpleRichTextBlock()),  # way 2
            ("card", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
        ],
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("fin_title"),
        FieldPanel("fin_subtitle"),
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Financial Blog"
        verbose_name_plural = "Financial Blog"
