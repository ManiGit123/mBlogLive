from django.urls import path
from . import views

urlpatterns = [
    path("db/", views.download_sqlite_db, name="download_sqlite_db"),
]
