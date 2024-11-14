from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone
from .models import CustomUser

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    user.last_login_time = timezone.now()
    user.last_login_ip = request.META.get('REMOTE_ADDR')
    user.save()