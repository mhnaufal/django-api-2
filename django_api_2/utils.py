"""
Helper to formatting the response API
based on the docs
"""
from rest_framework.response import Response


def send_success(payload, message, status):
    response = {"status": "SUCCESS", "message": message, "payload": payload}
    return Response(data=response, status=status)


def send_error(payload, message, status):
    response = {"status": "ERROR", "message": message, "payload": payload}
    return Response(data=response, status=status)
