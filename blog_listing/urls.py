from django.urls import path
from . import views

urlpatterns = [
    path("", views.hoempage, name="home_page"),
    path("db/", views.download_sqlite_db, name="download_sqlite_db"),
    path("robots.txt", views.robots_txt),
]
