from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from search import views as search_views

# from wagtail.contrib.sitemaps.views import sitemap as wagtail_sitemap
from django.contrib.sitemaps.views import sitemap as djsitemap
from .sitemaps import CombinedSitemap  # StaticViewSitemap  # , BlogSitemap


urlpatterns = [
    path(
        "sitemap.xml",
        djsitemap,
        {"sitemaps": {"combined": CombinedSitemap()}},
        name="sitemap",
    ),
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    path("", include("blog_listing.urls", namespace="blog_listing")),
    path("api/", include("api.urls")),
    path("tools/", include("tools.urls")),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
