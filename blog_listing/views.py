from django.shortcuts import render
from django.http import FileResponse, HttpResponse
import os
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from home.models import FinancialBLog, TravelBLog, TutorialsBLog

# Create your views here.


def hoempage(request):
    travel = TravelBLog.objects.live().public()
    fin = FinancialBLog.objects.live().public()
    tuto = TutorialsBLog.objects.live().public()
    context = {"travel": travel[0], "fin": fin[0], "tuto": tuto[0]}
    return render(request, template_name="home/landing_page.html", context=context)


@staff_member_required
def download_sqlite_db(request):
    db_path = os.path.join(settings.BASE_DIR, "db.sqlite3")

    if os.path.exists(db_path):
        if (
            request.user.username == "mani"
            and request.user.email == "manikandanp045@gmail.com"
        ):
            return FileResponse(
                open(db_path, "rb"), as_attachment=True, filename="db.sqlite3"
            )
        else:
            return HttpResponse("you are not allowed to access this path.", status=404)
    else:
        return HttpResponse("Database file not found.", status=404)


def robots_txt(request):
    content = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /search/",
        "Sitemap: https://mbloglive.onrender.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(content), content_type="text/plain")
