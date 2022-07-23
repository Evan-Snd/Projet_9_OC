from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from django.conf import settings


class UserFollows(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user',)
>>>>>>> f3dc60dde3dd6edbe4a2fcebb4307cc0156b0a30
