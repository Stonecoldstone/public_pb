from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework.permissions import IsAdminUser

from base.models import Creator
from base.serializers import CreatorSerializer



@api_view(['GET'])
@permission_classes([IsAdminUser])
def getCreators(request):

    creators        = Creator.objects.all()
    serializer      = CreatorSerializer(creators, many = True)

    return Response(serializer.data)



@api_view(['GET'])
def getCreator(request,pk):

    print("getCreator called.")
    creator        = Creator.objects.get(creator_id = pk)
    serializer     = CreatorSerializer(creator, many = False)

    return Response(serializer.data)

