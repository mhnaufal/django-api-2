from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Pengguna
from .serializers import PenggunaSerializer
from django_api_2.utils import send_error, send_success

@api_view(['GET'])
def get_users_data(request):
    queryset = Pengguna.objects.all()
    serializer = PenggunaSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user_data(request, id):
    try:
        queryset = Pengguna.objects.get(id=id)
    except Pengguna.DoesNotExist:
        return send_error(None, f"Gagal mendapatkan data pengguna dengan id {id}", status.HTTP_204_NO_CONTENT)
    
    serializer = PenggunaSerializer(queryset)
    return send_success(serializer.data, f"Berhasil mendapatkan data pengguna degan id {id}", status.HTTP_200_OK)