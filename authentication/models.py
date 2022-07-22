from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='suit'
    )
    followed_by = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='suivi par',
        related_name='followers'
    )
