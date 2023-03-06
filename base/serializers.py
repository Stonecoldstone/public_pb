from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, Creator
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):

    name        = serializers.SerializerMethodField(read_only = True)
    _id         = serializers.SerializerMethodField(read_only = True)
    isAdmin     = serializers.SerializerMethodField(read_only = True)

    class Meta:
        
        model   = User
        fields  = ['id', '_id', 'username', 'email', 'name', 'isAdmin']
        # https://docs.djangoproject.com/en/4.1/ref/contrib/auth/
        # User default attributes provided by Django

    def get__id(self, obj):
        """
        """
        return obj.id


    def get_isAdmin(self, obj):
        """
        """
        return obj.is_staff


    def get_name(self, obj):
        """
        Email is a required field, which is not the case for name.
        So let's just return the email in the name field if no name
        provided by used at sign in.
        """
        # Handles the case where there is no name, to avoid a server crash.
        if obj.is_authenticated:
            name = obj.first_name
            if name == '':
                name = obj.email
        else:
            name = 'Anonymous (not logged in)'
        return name


class UserSerializerWithToken(UserSerializer):

    token     = serializers.SerializerMethodField(read_only = True)


    class Meta:
        model   = User
        fields  = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    
    def get_token(self, obj):

        token = RefreshToken.for_user(obj)

        return str(token)



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        
        model   = Project
        fields  = '__all__'





class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        
        model   = Creator
        fields  = '__all__'