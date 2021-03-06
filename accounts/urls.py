from rest_framework_simplejwt import views as jwt_views
from . import views
from django.urls import path

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('user/login/', views.LoginView.as_view(), name="auth-login"),
    path('user/signup/', views.RegisterUsersView.as_view(), name="user-signup"),

]
