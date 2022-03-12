from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from core import views

urlpatterns = [
    path('', views.HelloView.as_view(), name='hello'),
    path('register/', views.Register.as_view()),
    path('login/', views.LoginPage.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
