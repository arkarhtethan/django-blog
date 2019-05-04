from .models import Post
from .serializers import PostSerailzier
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)

    permission_classes = (IsAuthenticated,)

    serializer_class = PostSerailzier

    queryset = Post.objects.all()

class LoginViewSet(viewsets.ViewSet):

    def create(self, request):

        return ObtainAuthToken().post(request)
    