
from rest_framework import (
    generics,
    authentication,
    permissions,
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


#Creates a new user
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


#Creates a new auth token for user
class CreateTokenView(ObtainAuthToken):

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


#Manages the authenticated user
class ManageUserView(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


    #Retrieves and returns authenticated user
    def get_object(self):
        return self.request.user