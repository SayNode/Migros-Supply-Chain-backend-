from django.urls import path
from .views import ListUserAPIView, RetrieveUserByIDAPIView, GetUserMeAPIView, SearchUserByStringAPIView, \
    RetrieveUserBalanceView, UpdateUserBalanceView

urlpatterns = [

    # backend/api/users/
    path('', ListUserAPIView.as_view()),
    #path('me/', RetrieveCurrentUserAPIView.as_view()),
    path('<int:pk>', RetrieveUserByIDAPIView.as_view()),
    path('balance/', RetrieveUserBalanceView.as_view()),
    path('balance/update/', UpdateUserBalanceView.as_view()),
    #path('me/', GetUserMeAPIView.as_view()),
    #path('?search', SearchUserByStringAPIView.as_view()),

]
