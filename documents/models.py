from pathlib import Path

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


def validate_pdf(file):
    if Path(file.name).suffix.lower() != ".pdf":
        raise ValidationError("Carica solo file PDF.")
    if file.size > 10 * 1024 * 1024:
        raise ValidationError("Il PDF non deve superare 10 MB.")


class UploadedDocument(models.Model):
    DOCUMENT_CHOICES = [
        ("diet", "Dieta"),
        ("meal_plan", "Piano alimentare"),
        ("workout", "Scheda allenamento"),
        ("running", "Piano corsa"),
        ("other", "Altro"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=160)
    document_type = models.CharField(max_length=24, choices=DOCUMENT_CHOICES, default="other")
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="documents/%Y/%m/", validators=[validate_pdf])
    extracted_text = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.title

