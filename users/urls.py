from django.urls import path
from .views import UsersViews,UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('users/', UsersViews.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("users/<int:user_id>/",UserDetailView.as_view())
]