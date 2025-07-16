from django import forms
from .models import WriterApplication


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
