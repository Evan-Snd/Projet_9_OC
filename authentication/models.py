from django.contrib.auth.models import AbstractUser
from django.db import models

<<<<<<< HEAD
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
=======

class User(AbstractUser):
    pass
>>>>>>> f3dc60dde3dd6edbe4a2fcebb4307cc0156b0a30
