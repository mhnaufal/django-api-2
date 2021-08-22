from rest_framework.response import Response
import json

def send_success(payload, message, status):
    payload = json.dumps(payload, default=str, indent=4)
    response = {"status": "SUCCESS", "message": message, "payload": payload}
    return Response(data=response, status=status)

def send_error(payload, message, status):
    payload = json.dumps(payload, default=lambda o: o.__dict__, indent=4)
    response = {"status": "ERROR", "message": message, "payload": payload}
    return Response(data=response, status=status)