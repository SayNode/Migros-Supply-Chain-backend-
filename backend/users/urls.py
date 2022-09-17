from django.urls import path
from .views import ListUserAPIView, RetrieveUserByIDAPIView, GetUserMeAPIView, SearchUserByStringAPIView

urlpatterns = [

    # backend/api/users/
    path('', ListUserAPIView.as_view()),
    #path('me/', RetrieveCurrentUserAPIView.as_view()),
    path('<int:pk>', RetrieveUserByIDAPIView.as_view()),
    #path('me/', GetUserMeAPIView.as_view()),
    #path('?search', SearchUserByStringAPIView.as_view()),

]
