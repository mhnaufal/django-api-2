from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from django.db import models


class Pengguna(models.Model):
    # Enumeration for StatusVerif column in table pengguna
    class StatusVerif(models.TextChoices):
        SUDAH = "SUDAH", _("sudah")
        BELUM = "BELUM", _("belum")


    # Columns in tabel pengguna
    nama = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=True, null=True, unique=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    no_hp = models.CharField(max_length=14, blank=True, null=True, unique=True)
    status_verif = models.CharField(
        max_length=5, choices=StatusVerif.choices, default=StatusVerif.BELUM
    )
    referral = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10, message="Kode referral tidak dikenali")],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
