from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status

from base.models import User
from base.serializers import UserSerializer, UserSerializerWithToken


from django.contrib.auth.hashers import make_password

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data

 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['POST'])
def registerUser(request):
    """
    Register a new user
    """

    requ_data   = request.data

    print(f'Data: {requ_data}')
    serializer  = UserSerializerWithToken(data = requ_data)

    try:
        if serializer.is_valid():
            # Create a new user object
            user = User.objects.create(
                first_name      =serializer.validated_data.get('first_name', ''),
                username        =serializer.validated_data['username'],
                email           =serializer.validated_data['email'],
                password        =make_password(serializer.validated_data.get('password'))
            )
            # Serialize the user object to return in the response
            serialized_user = UserSerializerWithToken(user)
            return Response(serialized_user.data, status=status.HTTP_201_CREATED)
        else:
            print(f"Serializer errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        message = {'detail':'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):

    user        = request.user
    serializer  = UserSerializer(user, many = False)

    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):

    users       = User.objects.all()
    serializer  = UserSerializer(users, many = True)

    return Response(serializer.data)


