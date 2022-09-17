from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.response import Response
from .serializers import UserSerializer

User = get_user_model()


# api/users/
class ListUserAPIView(ListAPIView):
    """
    List all Users

    Get request
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []


class ListUserAPIStatisticsView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []


class RetrieveUserByIDAPIView(RetrieveAPIView):
    """
    Retrieve User info by ID

    Retrieve User info by ID
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []


class SearchUserByStringAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(username__contains=request.kwargs.get('search_string'))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



# Get logged in user profile
class GetUserMeAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []


    def get(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    def patch(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



