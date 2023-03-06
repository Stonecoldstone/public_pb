from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework.permissions import IsAdminUser

from base.models import Project
from base.serializers import ProjectSerializer

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getProjects(request):

    projects    = Project.objects.all()
    serializer  = ProjectSerializer(projects, many = True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getProject(request,pk):

    print("getProject called.")
    project         = Project.objects.get(project_id = pk)
    serializer      = ProjectSerializer(project, many = False)

    return Response(serializer.data)

