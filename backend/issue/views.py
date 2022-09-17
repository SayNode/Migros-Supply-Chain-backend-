from rest_framework.response import Response
from rest_framework import filters, status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView




# Chapter views
from issue.models import Issue
from issue.serializers import IssueSerializer


class ListIssues(ListAPIView):
    """
        List all Issues

        Get request
    """


    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = []




class RetrieveIssueByCategoryID(ListAPIView):

    """
        List all Issues by Category ID

        Get request
    """

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = []

    def get_queryset(self):
        return self.queryset.filter(category__id=self.kwargs.get('pk'))

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if response.data:
            return response
        return Response(status=status.HTTP_404_NOT_FOUND)


class RetrieveIssueByProductID(ListAPIView):
    """
        List all Issues by Product ID

        Get request
    """

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = []

    def get_queryset(self):
        return self.queryset.filter(product__id=self.kwargs.get('pk'))

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if response.data:
            return response
        return Response(status=status.HTTP_404_NOT_FOUND)

class RetrieveIssueByUserID(ListAPIView):
    """
        List all Issues by User ID

        Get request
    """

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = []

    def get_queryset(self):
        return self.queryset.filter(user_id=self.kwargs.get('pk'))

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if response.data:
            return response
        return Response(status=status.HTTP_404_NOT_FOUND)


class CreateIssue(CreateAPIView):
    """
        Create a new issue

        Post request
    """

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = []



class RetrieveUpdateDestroyIssueByID(RetrieveUpdateDestroyAPIView):
    """
        GET:
        Retrieve issue by ID

        PUT:
        Update issue by entering all fields

        PATCH:
        Update issue (no all fields are required)

        DELETE:
        Delete issue by ID

    """

    queryset = Issue.objects.all().order_by('pk')
    serializer_class = IssueSerializer
    permission_classes = []
    lookup_field = 'id'



