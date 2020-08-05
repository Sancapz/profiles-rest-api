from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format=None):
        """return a list of API features"""
        an_apiview= [
            'use hhtp method as function(get,post,pactch,delete,put)',
            'is very similar to a traditional django view',
            'gives you the most control over your application logic',
            'is mapped manually to URLs',
        ]

        return Response({'message':'Hello!','an_apiview': an_apiview})
