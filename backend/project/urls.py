"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from allauth.account.views import ConfirmEmailView
from dj_rest_auth.registration.views import VerifyEmailView
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt import views as jwt_views

from project import settings
from registration_profile.views import GoogleLogin

schema_view = get_schema_view(
   openapi.Info(
      title="Zurich Hack Day API official Documentation",
      default_version='v1',
      description="Description of your Django App",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="riccardo@saynode.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,# Set to False restrict access to protected endpoints
   permission_classes=(permissions.AllowAny,),# Permissions for docs access
)





urlpatterns = [

    path('admin/', admin.site.urls),

#django allauth
    path('accounts/', include('allauth.urls')),

    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/account-confirm-email/', VerifyEmailView.as_view(), name='home'),
    path('confirm-email/<str:key>/', ConfirmEmailView.as_view(),
         name='account_confirm_email'),
    path('auth/google/', GoogleLogin.as_view()),

# Users
    path('api/users/', include('users.urls')),


# Registration
    #path('api/auth/registration/', include('registration_profile.urls')),

# login
    path('auth/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    #path('api/auth/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_refresh'),


# Categories
    path('api/category/', include('category.urls')),


# Issue
    path('api/issue/', include('issue.urls')),



#Api documentation
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

