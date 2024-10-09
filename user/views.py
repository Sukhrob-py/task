from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password

from .serializers import RegisterSerializer
from .models import User


class UserRegisterApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(username=request.POST.get("username"))
        user.set_password(request.POST.get("password"))
        user.is_active=True
        user.save()
        return Response({"user": serializer.data, "tokens": user.tokens()}, status=200)


class UserLoginApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.get(username=username)
        if check_password(password, user.password):
            return Response(
                {
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                    },
                    "tokens": user.tokens(),
                },
                status=200,
            )
        return Response({"error": "Invalid credentials"}, status=401)
