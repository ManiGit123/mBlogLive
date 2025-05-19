from django.shortcuts import render
from django.http import FileResponse, HttpResponse
import os
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def download_sqlite_db(request):
    db_path = os.path.join(settings.BASE_DIR, "db.sqlite3")

    if os.path.exists(db_path):
        return FileResponse(
            open(db_path, "rb"), as_attachment=True, filename="db.sqlite3"
        )
    else:
        return HttpResponse("Database file not found.", status=404)
