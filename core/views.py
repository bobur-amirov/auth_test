from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .serializers import RegisterSerializer

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class Register(APIView):
    def post(self, request):
        data = {}
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user).key
            data['token'] = token
            data['mess'] = "Foydalanuvchi yaratildi"
        else:
            data = serializer.errors
        return Response(data)


# class Register(APIView):
#     def post(self, request):
#         parser_classes = JSONParser
#         username = request.data['username']
#         email = request.data['email']
#         first_name = request.data['first_name']
#         last_name = request.data['last_name']
#         password = request.data['password']
#         user_check = User.objects.filter(username=username).exists()
#         if user_check:
#             return Response({'mess': "Bunaqa foydalanuvchi bor!"})
#         else:
#             user = User.objects.create_user(username, email, password)
#             user.first_name = first_name
#             user.last_name = last_name
#             user.save()
#             token, create = Token.objects.get_or_create(user=user)
#             return Response({'token': str(token)})


class LoginPage(APIView):
    def post(self, request):
        parser_classes = JSONParser
        username = request.data['username']
        password = request.data['password']
        if username is None or password is None:
            return Response({'mess': "Username yoki Password kiritmadingiz!"})
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'mess': "Username yoki Password xato!"})
        token, create = Token.objects.get_or_create(user=user)
        return Response({'token': str(token), 'mess': "Xush kelibsiz!"})