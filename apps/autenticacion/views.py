from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

class LoginView(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Credenciales no validas'}, status=status.HTTP_400_BAD_REQUEST)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class LogoutView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({'detail': 'Ha cerrado sesión correctamente'}, status=status.HTTP_200_OK)