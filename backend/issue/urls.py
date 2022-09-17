from django.urls import path
from .views import ListIssues, CreateIssue, RetrieveUpdateDestroyIssueByID, RetrieveIssueByCategoryID

urlpatterns = [
    #backend/api/issue/
    path('', ListIssues.as_view()),
    path('category/<int:pk>/', RetrieveIssueByCategoryID.as_view()),
    path('product/<int:pk>/', RetrieveIssueByCategoryID.as_view()),
    path('user/<int:pk>/', RetrieveIssueByCategoryID.as_view()),
    path('<int:id>/', RetrieveUpdateDestroyIssueByID.as_view()),
    path('new/', CreateIssue.as_view()),
]