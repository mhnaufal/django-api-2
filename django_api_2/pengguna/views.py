from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Pengguna
from .serializers import PenggunaSerializer, RegistrationSerializer
from django_api_2.utils import send_error, send_success


@api_view(["GET"])
def get_users_data(request):
    queryset = Pengguna.objects.all()
    serializer = PenggunaSerializer(queryset, many=True)
    return send_success(serializer.data, "Berhasil mendaptkan data semua pengguna", status=status.HTTP_200_OK)

@api_view(["GET"])
def get_user_data(request, id):
    try:
        queryset = Pengguna.objects.get(id=id)
    except Pengguna.DoesNotExist:
        return send_error(
            None,
            f"Gagal mendapatkan data pengguna dengan id {id}",
            status.HTTP_204_NO_CONTENT,
        )

    serializer = PenggunaSerializer(queryset)
    return send_success(
        serializer.data,
        f"Berhasil mendapatkan data pengguna degan id {id}",
        status.HTTP_200_OK,
    )

@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            pengguna = serializer.save()
            return send_success(pengguna, "Register berhasil", status.HTTP_200_OK)
        return send_error(None, "Register gagal. Silakan hubungi pihak Mulo untuk bantuan lebih lanjut", status.HTTP_400_BAD_REQUEST)