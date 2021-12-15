from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from .views import (
    ArticleAPIView,
    ArticleDetailAPIView,

    AddClientIPAddress,
    AddByUrl,

    RegisterUser)

urlpatterns =[
    path("api/",ArticleAPIView.as_view()),
    path("api/<int:pk>/",ArticleDetailAPIView.as_view()),

    path("api/add/",AddClientIPAddress.as_view()),
    path("api/add/<str:pk>/",AddByUrl.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("register/",RegisterUser.as_view()),
]