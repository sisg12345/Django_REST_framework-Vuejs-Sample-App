from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

app_name = 'auth'
urlpatterns = [
    path('login/', views.TokenObtainPairAPIView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path('register/', views.RegisiterAPIView.as_view(), name='auth_register'),
]