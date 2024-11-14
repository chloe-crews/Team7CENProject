from django.urls import path
from . import views
from django.contrib import admin
from django.views.generic import TemplateView
from .views import CreateUserView, DeleteUserView

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.signup, name='signup'),
    path('create-user/', CreateUserView.as_view(), name='create-user'),
    path('delete-user/<int:user_id>/', DeleteUserView.as_view(), name='delete-user'),
]