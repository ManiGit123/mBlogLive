# from django.contrib.sitemaps import Sitemap
# from django.urls import reverse
# from django.contrib.sites.models import Site
# from django.urls import reverse

# # from .models import YourModel  # import your models


# class StaticViewSitemap(Sitemap):
#     priority = 0.5
#     changefreq = "daily"
#     protocol = "https"  # Force HTTPS

#     # def get_urls(self, **kwargs):
#     #     current_site = Site.objects.get_current()
#     #     kwargs['domain'] = current_site.domain
#     #     return super().get_urls(**kwargs)

#     def items(self):
#         return ["home_page", "test"]  # list of view names

#     def location(self, item):
#         return reverse(item)


# # class BlogSitemap(Sitemap):
# #     changefreq = "weekly"
# #     priority = 0.7

# #     def items(self):
# #         return YourModel.objects.filter(is_published=True)

# #     def lastmod(self, obj):
# #         return obj.updated_at

from django.contrib.sitemaps import Sitemap
from wagtail.models import Page
from wagtail.contrib.sitemaps import Sitemap as WagtailSitemap
from blog_listing.models import MyImage  # Your Django model
from django.urls import reverse


class CombinedSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    protocol = "https"

    def items(self):
        # Get Wagtail pages
        wagtail_pages = list(WagtailSitemap().items())

        # Get Django model instances
        django_objects = list(MyImage.objects.all())

        # Static URLs (add your view names)
        static_urls = ["blog_listing:home_page", "blog_listing:test"]

        return wagtail_pages + static_urls + django_objects

    def location(self, item):
        if isinstance(item, Page):  # Wagtail page
            return item.get_url(request=None)  # request=None for simplicity
        elif isinstance(item, str):  # Static URL name
            try:
                return reverse(item)
            except:
                # If it fails, maybe it *is* a namespaced static URL from another app?
                # This part is more complex and depends on your specific setup.
                # For basic global pages, the first try should work.
                # If 'test' was, for example, 'my_other_app:test_view', you'd need another condition.
                # For now, let's assume if it fails here, it's truly not found globally.
                print(f"Warning: Could not reverse global URL: {item}")
                return None  # Or raise an error if this should never happen
        elif isinstance(item, MyImage):  # Django model instance
            # Use your actual detail view name here
            return reverse("blog_listing:myimage-detail", kwargs={"pk": item.pk})
            # Or if using slug: kwargs={'slug': item.slug}

    def lastmod(self, item):
        if isinstance(item, Page):  # Wagtail page
            return item.last_published_at
        elif hasattr(item, "updated_at"):
            return item.updated_at
        return None  # Static URLs don't need lastmod
