from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import models, serializers, permissions
from django.contrib.auth.models import User

class HelloApiView(APIView):
    # The Test API view
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
        ]

        return Response ({'message':"Hello!", "an_apiview":an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message":message})
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, pk=None):
        # Handle update an object
        return Response ({'method':"PUT"})

    def patch (self, request, pk=None):
        # Handle a partial update of an obejct
        return Response({"method":"PATCH"})

    def delete(self, request, pk=None):
        # Delete an object
        return Response({"method":"DELETE"})



class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        # Return a hello message
        a_viewset = [
            'Uses actions (list, create, retrieve)',
            'Automatically maps to URL using routers',
            'Provides more with less code'
        ]

        return Response({"message":"hello", "a_viewset":a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=404
            )

    def retrieve(self, request, pk=None):
        return Response({"http_method":"GET"})


    def update(self, request, pk=None):
        return Response({"http_method":"PUT"})


    def partial_update(self, request, pk=None):
        return Response({"http_method":"PATCH"})

    def destroy(self, request, pk=None):
        return Response({"http_method":"DELETE"})
        

class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'email')


class UserLoginApiView(ObtainAuthToken):
    # Create user authentication tokens
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    #Handles creating, reading and updating profile feed items
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeed.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)

         