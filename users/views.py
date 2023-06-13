from django.shortcuts import render
from rest_framework.views import APIView,Request,Response,status
from users.models import User
from users.serializers import UserSerializer

class UsersViews(APIView):
 def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
