from django import forms
from .models import WriterApplication
from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-3 border border-gray-300 dark:border-gray-700 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:text-gray-200",
                    "required": "required",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "w-full px-4 py-3 border border-gray-300 dark:border-gray-700 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:text-gray-200",
                    "required": "required",
                }
            ),
            "subject": forms.Select(
                attrs={
                    "class": "w-full px-4 py-3 border border-gray-300 dark:border-gray-700 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:text-gray-200"
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "w-full px-4 py-3 border border-gray-300 dark:border-gray-700 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:text-gray-200",
                    "rows": "3",
                    "required": "required",
                }
            ),
        }


class WriterApplicationForm(forms.ModelForm):
    class Meta:
        model = WriterApplication
        fields = [
            "name",
            "email",
            "topic",
            "article_idea",
            "writing_experience",
            "writing_samples",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Map your custom field names to model fields
        self.fields["article_idea"].widget.attrs.update({"id": "article-idea"})
        self.fields["writing_experience"].widget.attrs.update({"id": "experience"})
        self.fields["writing_samples"].widget.attrs.update({"id": "samples"})
