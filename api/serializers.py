from rest_framework import serializers
from .models import Location
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken

User=get_user_model()

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model =Location
        fields= "__all__"


class UserSerializerWithToken(serializers.HyperlinkedModelSerializer):
    token= serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ('username','password','token')
        extra_kwargs = {'password' : {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def get_token(self,obj):
        token=AccessToken.for_user(obj)
        return str(token)