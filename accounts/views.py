from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import Helpr_User_Serializer
from .models import Helpr_User
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.


class Accounts_List(APIView):


    def get(self, request):

        helpr_users = Helpr_User.objects.all()
        serialized_helpr_users = Helpr_User_Serializer(helpr_users, many=True)

        return Response(serialized_helpr_users.data)

    def post(self, request):

        created_user = User.objects.create_user(
            request.data['username'],
            request.data['email'],
            request.data['password']
        )

        serialized_user = Helpr_User_Serializer(created_user.helpr_user, many=False)

        return Response(serialized_user.data)
