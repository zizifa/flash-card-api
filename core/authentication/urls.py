from django.urls import path
# from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import CreateUserView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#use simplejwt
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),#use simplejwt
    path('register/', CreateUserView.as_view(), name="sign_up"),
]