from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from . import blocks
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtailcodeblock.blocks import CodeBlock
from wagtailseo.models import SeoMixin, SeoType, TwitterCard
from wagtail.embeds.blocks import EmbedBlock

# from modelcluster.fields import ParentalKey


class HomePage(SeoMixin, Page):
    template = "home/home_page.html"
    # max_count = 1  # restrict child
    banner_title = models.CharField(max_length=300, blank=False, null=True)
    banner_subtitle = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
    ]
    promote_panels = SeoMixin.seo_panels


class FinancialBLog(SeoMixin, Page):
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
            ("codeblock", CodeBlock(label="Code block", classname="container")),
            ("embedded", EmbedBlock()),
            ("date_picker", blocks.DatePickerBlock()),
            ("button_link", blocks.ButtonLinkBlock()),
        ],
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("fin_title"),
        FieldPanel("fin_subtitle"),
        FieldPanel("content"),
    ]
    # Indicate this is article-style content.
    seo_content_type = SeoType.ARTICLE

    # Change the Twitter card style.
    seo_twitter_card = TwitterCard.LARGE

    promote_panels = SeoMixin.seo_panels

    class Meta:
        verbose_name = "Financial Blog"
        verbose_name_plural = "Financial Blogs"


class TravelBLog(SeoMixin, Page):
    template = "travel/travel_page.html"
    travel_title = models.CharField(max_length=300, blank=False, null=True)
    travel_subtitle = RichTextField(blank=True)
    content = StreamField(
        [
            ("title_and_text", blocks.TitleandTexBlock()),
            ("rich_text", blocks.RichTextBlock()),
            ("simple_rich_text", blocks.SimpleRichTextBlock()),  # way 2
            ("card", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
            ("codeblock", CodeBlock(label="Code block", classname="container")),
            ("embedded", EmbedBlock()),
            ("date_picker", blocks.DatePickerBlock()),
            ("button_link", blocks.ButtonLinkBlock()),
        ],
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("travel_title"),
        FieldPanel("travel_subtitle"),
        FieldPanel("content"),
    ]
    # Indicate this is article-style content.
    seo_content_type = SeoType.ARTICLE

    # Change the Twitter card style.
    seo_twitter_card = TwitterCard.LARGE

    promote_panels = SeoMixin.seo_panels

    class Meta:
        verbose_name = "Travel Blog"
        verbose_name_plural = "Travel Blogs"


class TutorialsBLog(SeoMixin, Page):
    template = "tuto/tuto_page.html"
    tuto_title = models.CharField(max_length=300, blank=False, null=True)
    tuto_subtitle = RichTextField(blank=True)
    content = StreamField(
        [
            ("title_and_text", blocks.TitleandTexBlock()),
            ("rich_text", blocks.RichTextBlock()),
            ("simple_rich_text", blocks.SimpleRichTextBlock()),  # way 2
            ("card", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
            ("codeblock", CodeBlock(label="Code block", classname="container")),
            ("embedded", EmbedBlock()),
            ("date_picker", blocks.DatePickerBlock()),
            ("button_link", blocks.ButtonLinkBlock()),
        ],
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("tuto_title"),
        FieldPanel("tuto_subtitle"),
        FieldPanel("content"),
    ]
    # Indicate this is article-style content.
    seo_content_type = SeoType.ARTICLE

    # Change the Twitter card style.
    seo_twitter_card = TwitterCard.LARGE

    promote_panels = SeoMixin.seo_panels

    class Meta:
        verbose_name = "Tutorial Blog"
        verbose_name_plural = "Tutorial Blogs"
