from django.urls import path


from core import views

urlpatterns = [
    path('', views.HelloView.as_view(), name='hello'),
    path('register/', views.Register.as_view()),
    path('login/', views.LoginPage.as_view()),
]
