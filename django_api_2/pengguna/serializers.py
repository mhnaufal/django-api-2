from django_api_2.pengguna.models import Pengguna
from rest_framework import serializers

class PenggunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengguna
        fields = ['id', 'nama', 'email', 'no_hp', 'referral', 'created_at', 'updated_at']