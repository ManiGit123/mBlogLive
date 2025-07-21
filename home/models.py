from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from . import blocks
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtailcodeblock.blocks import CodeBlock
from wagtailseo.models import SeoMixin, SeoType, TwitterCard
from wagtail.embeds.blocks import EmbedBlock
from wagtail.contrib.table_block.blocks import TableBlock

# from modelcluster.fields import ParentalKey


class HomePage(SeoMixin, Page):
    template = "home/home_page.html"
    max_count = 1  # restrict child
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
    fin_subtitle = RichTextField(blank=False, null=True)
    fin_type = models.CharField(
        max_length=50,
        choices=[
            ("option1", "Personal Finance"),
            ("option2", "Investments"),
            ("option3", "Retirement"),
            ("option4", "Debt"),
        ],
        default="option1",
        null=True,
        blank=False,
    )
    fin_date = models.DateField("Post date", blank=False, null=True)
    fin_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    content = StreamField(
        [
            ("title_and_text", blocks.TitleandTexBlock()),
            ("rich_text", blocks.RichTextBlock()),
            ("simple_rich_text", blocks.SimpleRichTextBlock()),  # way 2
            ("card", blocks.CardBlock()),
            ("carousel", blocks.CarouselBlock()),
            ("accordion", blocks.AccordionBlock()),
            ("cta", blocks.CTABlock()),
            ("cuscodeblock", blocks.CustomCodeBlock()),
            ("codeblock", CodeBlock(label="Code block", classname="container")),
            ("embedded", EmbedBlock()),
            ("date_picker", blocks.DatePickerBlock()),
            ("button_link", blocks.ButtonLinkBlock()),
            ("table", TableBlock()),
        ],
        blank=True,
        null=True,
        collapsed=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("fin_title"),
                FieldPanel("fin_subtitle"),
                FieldPanel("fin_image"),
                FieldPanel("fin_type"),
                FieldPanel("fin_date"),
            ],
            heading="Banner Options",
            classname="collapsible collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel("content"),
            ],
            heading="Stream Options",
            classname="collapsible collapsed",
        ),
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
    travel_location = models.CharField(max_length=300, blank=False, null=True)
    travel_date = models.DateField("Post date", blank=False, null=True)
    travel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    content = StreamField(
        [
            ("title_and_text", blocks.TitleandTexBlock()),
            ("rich_text", blocks.RichTextBlock()),
            ("simple_rich_text", blocks.SimpleRichTextBlock()),  # way 2
            ("card", blocks.CardBlock()),
            ("carousel", blocks.CarouselBlock()),
            ("accordion", blocks.AccordionBlock()),
            ("cta", blocks.CTABlock()),
            ("cuscodeblock", blocks.CustomCodeBlock()),
            ("codeblock", CodeBlock(label="Code block", classname="container")),
            ("embedded", EmbedBlock()),
            ("date_picker", blocks.DatePickerBlock()),
            ("button_link", blocks.ButtonLinkBlock()),
            ("table", TableBlock()),
        ],
        blank=True,
        null=True,
        collapsed=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("travel_title"),
                FieldPanel("travel_subtitle"),
                FieldPanel("travel_location"),
                FieldPanel("travel_date"),
                FieldPanel("travel_image"),
            ],
            heading="Banner Options",
            classname="collapsible collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel("content"),
            ],
            heading="Stream Options",
            classname="collapsible collapsed",
        ),
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
    tuto_learner_type = models.CharField(
        max_length=50,
        choices=[
            ("option1", "Beginner"),
            ("option2", "Intermediate"),
            ("option3", "Advanced"),
            ("option4", "Expert"),
        ],
        default="option1",
        null=True,
        blank=False,
    )
    tuto_duration = models.CharField(max_length=300, blank=False, null=True)
    tuto_date = models.DateField("Post date", blank=False, null=True)
    tuto_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    content = StreamField(
        [
            ("title_and_text", blocks.TitleandTexBlock()),
            ("rich_text", blocks.RichTextBlock()),
            ("simple_rich_text", blocks.SimpleRichTextBlock()),  # way 2
            ("card", blocks.CardBlock()),
            ("carousel", blocks.CarouselBlock()),
            ("accordion", blocks.AccordionBlock()),
            ("cta", blocks.CTABlock()),
            ("cuscodeblock", blocks.CustomCodeBlock()),
            ("codeblock", CodeBlock(label="Code block", classname="container")),
            ("embedded", EmbedBlock()),
            ("date_picker", blocks.DatePickerBlock()),
            ("button_link", blocks.ButtonLinkBlock()),
            ("table", TableBlock()),
        ],
        blank=True,
        null=True,
        collapsed=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("tuto_title"),
                FieldPanel("tuto_subtitle"),
                FieldPanel("tuto_learner_type"),
                FieldPanel("tuto_duration"),
                FieldPanel("tuto_date"),
                FieldPanel("tuto_image"),
            ],
            heading="Banner Options",
            classname="collapsible collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel("content"),
            ],
            heading="Stream Options",
            classname="collapsible collapsed",
        ),
    ]
    # Indicate this is article-style content.
    seo_content_type = SeoType.ARTICLE

    # Change the Twitter card style.
    seo_twitter_card = TwitterCard.LARGE

    promote_panels = SeoMixin.seo_panels

    class Meta:
        verbose_name = "Tutorial Blog"
        verbose_name_plural = "Tutorial Blogs"


news_cat_choices = [
    ("option1", "Business"),
    ("option2", "Technology"),
    ("option3", "Science"),
    ("option4", "Health"),
    ("option5", "Sports"),
    ("option6", "Entertainment"),
]


class NewsArticle(SeoMixin, Page):

    template = "news/news_page.html"
    news_title = models.CharField(max_length=300, blank=False, null=True)
    news_subtitle = RichTextField(blank=True)
    news_categories = models.CharField(
        max_length=50,
        choices=news_cat_choices,
        default="option1",
        null=True,
        blank=False,
    )
    news_date = models.DateField("Post date", blank=False, null=True)
    news_author = models.ForeignKey(
        "blog_listing.NewsAuthor",  # Reference the snippet
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="posts",
    )
    news_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    content = StreamField(
        [
            ("title_and_text", blocks.TitleandTexBlock()),
            ("rich_text", blocks.RichTextBlock()),
            ("simple_rich_text", blocks.SimpleRichTextBlock()),  # way 2
            ("card", blocks.CardBlock()),
            ("carousel", blocks.CarouselBlock()),
            ("accordion", blocks.AccordionBlock()),
            ("cta", blocks.CTABlock()),
            ("cuscodeblock", blocks.CustomCodeBlock()),
            ("codeblock", CodeBlock(label="Code block", classname="container")),
            ("embedded", EmbedBlock()),
            ("date_picker", blocks.DatePickerBlock()),
            ("button_link", blocks.ButtonLinkBlock()),
            ("table", TableBlock()),
        ],
        blank=True,
        null=True,
        collapsed=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("news_title"),
                FieldPanel("news_subtitle"),
                FieldPanel("news_categories"),
                FieldPanel("news_date"),
                FieldPanel("news_author"),
                FieldPanel("news_image"),
            ],
            heading="Banner Options",
            classname="collapsible collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel("content"),
            ],
            heading="Stream Options",
            classname="collapsible collapsed",
        ),
    ]
    # Indicate this is article-style content.
    seo_content_type = SeoType.ARTICLE

    # Change the Twitter card style.
    seo_twitter_card = TwitterCard.LARGE

    # Add Open Graph settings
    seo_og_type = "article"  # Explicitly set OG type

    promote_panels = SeoMixin.seo_panels

    class Meta:
        verbose_name = "News Article"
        verbose_name_plural = "News Articles"
