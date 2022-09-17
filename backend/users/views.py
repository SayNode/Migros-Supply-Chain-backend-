from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer, UserBalanceSerializer, UpdateBalanceSerializer

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


class RetrieveUserBalanceView(ListAPIView):
    """
    Retrieve User Balance

    Retrieve User Balance
    """

    queryset = User.objects.all()
    serializer_class = UserBalanceSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.pk)




class UpdateUserBalanceView(UpdateAPIView):
    """
    Update User Balance

    Update User Balance
    """

    queryset = User.objects.all()
    serializer_class = UpdateBalanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(pk=self.request.user.id)

    def update(self, request, *args, **kwargs):
        user_request_token = request.data.get("balance")
        current_balance = User.objects.filter(id=request.user.pk)
        get_amount = current_balance[0].balance

        User.objects.update(
                            balance= get_amount + user_request_token
                            )

        return Response({'message': "Your balance was successfully updated"}, status=status.HTTP_201_CREATED)


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



