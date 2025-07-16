from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from home import blocks
from home.models import FinancialBLog, TravelBLog, TutorialsBLog
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from django.core.validators import URLValidator

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

        # Get all blog posts ordered by date
        blog_posts = FinancialBLog.objects.live().public()

        # Pagination
        page = request.GET.get("page")
        paginator = Paginator(blog_posts, 10)  # Show 10 posts per page

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        contaxt["posts"] = posts
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
        # Get all blog posts ordered by date
        blog_posts = TravelBLog.objects.live().public()

        # Pagination
        page = request.GET.get("page")
        paginator = Paginator(blog_posts, 10)  # Show 10 posts per page

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        contaxt["posts"] = posts
        return contaxt


class TutorialsBlogListingPage(Page):
    # getting all the blogdetailpages and putting them into then context of this template
    # listing page lists all blog details pages

    template = "tuto/tuto_blog_listing_page.html"

    custom_title = models.CharField(
        max_length=100, blank=False, null=False, help_text="Overwrite the default title"
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        # Adding custom stuff to our contaxt
        contaxt = super().get_context(request, *args, **kwargs)
        # Get all blog posts ordered by date
        blog_posts = TutorialsBLog.objects.live().public()

        # Pagination
        page = request.GET.get("page")
        paginator = Paginator(blog_posts, 10)  # Show 10 posts per page

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        contaxt["posts"] = posts
        return contaxt


class MyImage(models.Model):
    image = models.ImageField()


TOPIC_CHOICES = [
    ("travel", "Travel Guides"),
    ("finance", "Finance & Budgeting"),
    ("technology", "Tech Tutorials"),
    ("remote-work", "Remote Work"),
    ("lifestyle", "Lifestyle"),
    ("other", "Other"),
]


class WriterApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    article_idea = models.CharField(max_length=200)
    writing_experience = models.TextField()
    writing_samples = models.TextField(
        blank=True,
        null=True,
        validators=[URLValidator()],
        help_text="Please provide links to your published work (comma separated if multiple)",
    )
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f"Application from {self.name} - {self.get_topic_display()}"

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "Writer Application"
        verbose_name_plural = "Writer Applications"
