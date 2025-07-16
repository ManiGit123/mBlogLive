from django.urls import path
from . import views

# ----> added for sitemap combining namespace for this urls.py
app_name = "blog_listing"

urlpatterns = [
    path("", views.homepage, name="home_page"),
    path("about-us/", views.AboutUs, name="about_us"),
    path("contact-us/", views.ContactUs, name="contact_us"),
    path("privacy-policy/", views.PrivacyPolicy, name="privacy_policy"),
    path("terms-of-service/", views.TermsofService, name="terms_of_service"),
    path(
        "submit-writer-application/",
        views.submit_writer_application,
        name="submit_writer_application",
    ),
    path("test/", views.test, name="test"),
    path("db/", views.download_sqlite_db, name="download_sqlite_db"),
    path("robots.txt", views.robots_txt),
    path("myimage/<int:pk>/", views.MyImageDetailView.as_view(), name="myimage-detail"),
]
