from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse
import os
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from home.models import FinancialBLog, TravelBLog, TutorialsBLog
from django.views.generic import DetailView
from .models import MyImage
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import WriterApplicationForm
from django.views.decorators.csrf import csrf_exempt
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import ContactSubmission
from .forms import NewsletterForm
from .models import NewsletterSubscriber


def homepage(request):
    travel = TravelBLog.objects.live().public()
    fin = FinancialBLog.objects.live().public()
    tuto = TutorialsBLog.objects.live().public()

    # Landing page form handling
    if request.method == "POST" and "landing_form" in request.POST:
        form = NewsletterForm(request.POST)
        # print(f"Form is valid: {form.is_valid()}")  # Debug line
        # print(f"Form errors: {form.errors}")  # Debug line
        if form.is_valid():
            subscriber = form.save(commit=False)
            subscriber.source = "landing"
            subscriber.save()
            messages.success(
                request, "Thank you for subscribing!", extra_tags="landing_form"
            )
            return redirect("blog_listing:home_page")
        else:
            # Pass form errors to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}", extra_tags="landing_form")
    else:
        form = NewsletterForm()

    context = {
        "travel": travel[len(travel) - 1],
        "fin": fin[len(fin) - 1],
        "tuto": tuto[len(tuto) - 1],
        "landing_form": form,
    }
    return render(request, "home/landing_page.html", context)


def footer_subscribe(request):
    if request.method == "POST":
        # print("footer POST data:", request.POST)
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subscriber = form.save(commit=False)
            subscriber.source = "footer"
            subscriber.save()
            messages.success(
                request, "Thank you for subscribing!", extra_tags="footer_form"
            )
        else:
            for error in form.errors.get("email", []):
                messages.error(request, error, extra_tags="footer_form")
            # messages.error(request, "Please enter a valid email address")
        return redirect(request.META.get("HTTP_REFERER", "home"))


def AboutUs(request):
    return render(request, template_name="home/about_us.html")


@staff_member_required
def toggle_reviewed(request, pk):  # This is for admin review
    submission = get_object_or_404(ContactSubmission, pk=pk)
    submission.reviewed = not submission.reviewed
    submission.save()
    return redirect("admin:blog_listing_contactsubmission_changelist")


def ContactUs(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for contacting us! We will get back to you soon.",
                extra_tags="contact_form",
            )
            return redirect("blog_listing:contact_us")
        else:
            for error in form.errors.get("email", []):
                messages.error(request, error, extra_tags="contact_form")
    else:
        form = ContactForm()

    return render(request, template_name="home/contact_us.html", context={"form": form})


def PrivacyPolicy(request):
    return render(request, template_name="home/privacy_policy.html")


def TermsofService(request):
    return render(request, template_name="home/terms_of_service.html")


@require_POST
def submit_writer_application(request):
    try:
        # For debugging - print raw POST data
        # print("Raw POST data:", request.POST)

        form = WriterApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            return JsonResponse(
                {
                    "status": "success",
                    "message": "Application submitted successfully!",
                    "id": application.id,
                }
            )
        else:
            print("Form errors:", form.errors.as_json())
            return JsonResponse(
                {
                    "status": "error",
                    "message": "Please correct the errors below.",
                    "errors": json.loads(form.errors.as_json()),
                },
                status=400,
            )
    except Exception as e:
        print("Server error:", str(e))
        return JsonResponse(
            {"status": "error", "message": "Server error: " + str(e)}, status=500
        )


def test(request):
    return render(request, template_name="home/test.html")


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
        "Sitemap: https://www.maptomoney.in/sitemap.xml",
    ]
    return HttpResponse("\n".join(content), content_type="text/plain")


class MyImageDetailView(DetailView):
    model = MyImage  # Your model name
    template_name = "common/my_image.html"  # Your template path
    context_object_name = "image"  # Variable name in template

    def get_queryset(self):
        # Only show published products
        return super().get_queryset().filter(id=self.kwargs["pk"])
