from django.urls import path, include
from django.contrib import admin
from .views import SignUpView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/account', include('django.contrib.auth.urls')),
]
