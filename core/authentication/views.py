from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import CreateUserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response


class CreateUserView(APIView):
    def post(self,request):
        req_data=request.data
        serializer=CreateUserSerializer(data=req_data)
        serializer.is_valid(raise_exception=True)

        # we have to save user password so ...
        data = serializer.validated_data #take validate data from serializer
        user_data=User(
            username=data['username'],
            email=data['email']
        )
        user_data.set_password(data['password'])
        user_data.save()
        return Response(serializer.data)



