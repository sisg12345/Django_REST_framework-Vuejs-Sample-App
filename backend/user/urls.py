from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('user/', views.UserAPIView.as_view()),
    path('user/<pk>/', views.UserAPIView.as_view()),
    path('userList/', views.UserListAPIView.as_view())
]