from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from views import AddCostumeView

urlpatterns = [
    path('', views.costume_list, name='home'),  # Redirect '/' to costume list if desired
    path('signup/', views.signup, name='signup'),
    path('login/', views.home, name='login'),
    path('costumes/', views.costume_list, name='costume_list'),
    path('costumes/add/', AddCostumeView.as_view(), name='add_costume'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
]
