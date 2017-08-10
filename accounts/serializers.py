from rest_framework import serializers
from .models import Helpr_User
from django.contrib.auth.models import User



class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class Helpr_User_Serializer(serializers.ModelSerializer):
    user = User_Serializer(many=False, read_only=True)

    class Meta:
        model = Helpr_User
        fields = "__all__"
