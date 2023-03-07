from rest_framework.decorators import api_view
from rest_framework.response import Response

"""
Serialization in the context of a Django application refers to the process of converting 
complex Python objects into a format that can be easily stored, transmitted, and 
reconstructed later.

In Django, serialization is often used to convert database objects, such as model 
instances, into a format that can be transferred over the network, such as JSON or XML. 
This allows data to be easily shared between different systems or applications.
"""


"""
https://github.com/jazzband/djangorestframework-simplejwt/blob/master/rest_framework_simplejwt/serializers.py
"""

@api_view(['GET'])
def getRoutes(request):
    """
    """
    print("getRoutes called.")

    routes = [
        '/api/users/profile/',
        '/api/articles/',
        '/api/projects/',
        '/api/creators/',
        '/api/creator/',
        '/api/creator/<id>/',
        '/api/project/<id>/',
        '/api/project/<id>/',
        '/api/creators/login/'
    ]

    return Response(routes)


