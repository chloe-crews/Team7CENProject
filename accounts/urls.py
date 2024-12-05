from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.costume_list, name='home'),  
    path('signup/', views.signup, name='signup'),
    path('login/', views.home, name='login'), 
    path('costumes/', views.costume_list, name='costume_list'),
    path('costumes/<int:pk>/', views.costume_detail, name='costume_detail'), 
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('add-listing/', views.add_listing, name='add_listing'),
    path('update-profile-picture/', views.update_profile_picture, name='update_profile_picture'),
    path('profile/<str:username>/update/', views.update_profile, name='update_profile'),
    path('costumes/<int:pk>/edit/', views.edit_costume, name='edit_costume'),
    path('costumes/<int:pk>/delete/', views.delete_costume_confirmation, name='delete_costume'),
    path('costumes/<int:costume_id>/message/', views.send_message, name='send_message'),
    path('messages/', views.view_messages, name='view_messages'),
    path('inbox/', views.user_inbox, name='user_inbox'),
    path('messages/delete/<int:message_id>/', views.delete_message, name='delete_message'),
]

if settings.DEBUG:  # Serve media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
