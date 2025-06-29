from django.urls import path
from . import views

# ----> added for sitemap combining namespace for this urls.py
app_name = "blog_listing"

urlpatterns = [
    path("", views.hoempage, name="home_page"),
    path("test/", views.test, name="test"),
    path("db/", views.download_sqlite_db, name="download_sqlite_db"),
    path("robots.txt", views.robots_txt),
    path("myimage/<int:pk>/", views.MyImageDetailView.as_view(), name="myimage-detail"),
]
