from django.urls import path

from .views import ListCategories, CreateCategory, RetrieveUpdateDestroyCategoryByID, \
    SearchCategoryByStringAPIView

urlpatterns = [
    #backend/api/category/
    path('', ListCategories.as_view()),
    #path('<int:id>/', RetrieveUpdateDestroyCategoryByID.as_view()),
    #path('new/', CreateCategory.as_view()),
    #path('search/', SearchCategoryByStringAPIView.as_view()),
]