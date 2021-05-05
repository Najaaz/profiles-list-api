from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    # The Test API view

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
        ]

        return Response ({'message':"Hello!", "an_apiview":an_apiview})

