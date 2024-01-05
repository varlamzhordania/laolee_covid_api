from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime


class CovidCase(models.Model):
    class ImportedLocalChoices(models.TextChoices):
        IMPORTED = "Imported", _("Imported")
        LOCAL = "Local", _("Local")

    class StatusChoices(models.TextChoices):
        HOSPITALISED = "Hospitalised", _("Hospitalised")
        DISCHARGED = "Discharged", _("Discharged")

    case_id = models.CharField(
        max_length=50,
        verbose_name=_("Case ID"),
        help_text=_("Format: max-50, required"),
        unique=True,
    )
    age = models.PositiveSmallIntegerField(
        verbose_name=_("Age"),
        default=1,
        help_text=_("Format: positive integer, required"),
    )
    gender = models.CharField(
        max_length=1,
        choices=[("M", _("Male")), ("F", _("Female"))],
        default="M",
        verbose_name=_("Gender"),
        help_text=_("Format: max-1, M=Male, F=Female, default=M, required"),
    )
    nationality = models.CharField(
        max_length=255,
        verbose_name=_("Nationality"),
        blank=True,
        null=True,
        help_text=_("Format: max-255"),
    )
    imported_local = models.CharField(
        max_length=10,
        choices=ImportedLocalChoices.choices,
        verbose_name=_("Imported Local"),
        blank=True,
        null=True,
    )
    place = models.CharField(
        max_length=255,
        verbose_name=_("Place"),
        blank=True,
        null=True,
        help_text=_("Format: max-255"),
    )
    public_healthcare_institution = models.CharField(
        max_length=255,
        verbose_name=_("Public Healthcare Institution"),
        blank=True,
        null=True,
        help_text=_("Format: max-255"),
    )
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.HOSPITALISED,
        verbose_name=_("Status"),
        help_text=_("Format: required, default=Hospitalised"),
    )
    date_of_confirmation = models.DateField(
        verbose_name=_("Date of Confirmation"),
        default=datetime.now,
        help_text=_("Format: YYYY-MM-DD"),
    )
    date_of_discharge = models.DateField(
        verbose_name=_("Date of Discharge"),
        null=True,
        blank=True,
        help_text=_("Format: YYYY-MM-DD"),
    )
    places_visited = models.TextField(
        verbose_name=_("Places Visited"),
        max_length=3000,
        blank=True,
        null=True,
        help_text=_("Format: max-3000"),
    )
    residing_location = models.CharField(
        max_length=100,
        verbose_name=_("Residing Location"),
        help_text=_("Format: max-100, required"),
    )
    residing_postal_code = models.CharField(
        max_length=10,
        verbose_name=_("Residing Postal Code"),
        help_text=_("Format: max-10, required"),
    )
    reference_url = models.URLField(
        verbose_name=_("Reference URL"),
        help_text=_("Format: Valid URL, required"),
    )

    class Meta:
        verbose_name = _("CovidCase")
        verbose_name_plural = _("CovidCases")
        ordering = ["-id"]

    def __str__(self):
        return f"{self.case_id} - {self.get_status_display()}"
