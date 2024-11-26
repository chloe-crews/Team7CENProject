from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.costume_list, name='home'),  # Redirect '/' to costume list if desired
    path('signup/', views.signup, name='signup'),
    path('login/', views.home, name='login'), 
    path('costumes/', views.costume_list, name='costume_list'),
    path('costumes/<int:pk>/', views.costume_detail, name='costume_detail'),  # View costume details
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('add-listing/', views.add_listing, name='add_listing'),
    path('update-profile-picture/', views.update_profile_picture, name='update_profile_picture'),
    path('profile/<str:username>/update/', views.update_profile, name='update_profile'),
    path('costumes/<int:pk>/edit/', views.edit_costume, name='edit_costume'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
