from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password, check_password
from django_api_2.pengguna.models import Pengguna


class PenggunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengguna
        fields = [
            "id",
            "nama",
            "email",
            "no_hp",
            "referral",
            "created_at",
            "updated_at",
        ]


class RegistrationSerializer(serializers.ModelSerializer):
    # Validation fields which is use for register
    # validation errors goes inside here
    nama = serializers.CharField(default="User Mulo")

    email = serializers.EmailField(
        required=False,
        validators=[
            UniqueValidator(
                queryset=Pengguna.objects.all(),
                message="Email sudah terdaftar. Silakan gunakan email yang lain atau jika Anda merasa belum mendaftarkan email Anda di Mulo, silakan hubungi kontak Mulo untuk bantuan lebih lanjut!",
            )
        ],
    )

    no_hp = serializers.CharField(
        # default=None,
        required=False,
        validators=[
            UniqueValidator(
                queryset=Pengguna.objects.all(),
                message="Nomor hp sudah terdaftar. Silakan gunakan nomor hp yang lain atau jika Anda merasa belum mendaftarkan nomor hp Anda di Mulo, silakan hubungi kontak Mulo untuk bantuan lebih lanjut!",
            )
        ],
        min_length=11,
        max_length=14,
        error_messages={"message": "Bukan nomor hp"},
    )

    password = serializers.CharField(
        write_only=True,
        required=False,
        min_length=8,
        error_messages={"message": "Panjang minimum password adalah 8 karakter"},
    )

    # Define the model for registration
    class Meta:
        model = Pengguna
        fields = ["nama", "email", "password", "no_hp"]

    # Register the user and save it into database
    def save(self):
        pengguna = Pengguna(
            nama=self.validated_data["nama"],
            email=self.validated_data["email"],
            no_hp=self.validated_data["no_hp"],
            password=make_password(self.validated_data["password"]),
        )
        pengguna.save()
        return pengguna
