from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models

from PIL import Image


class Ticket(models.Model):
    title = models.CharField(max_length=128, verbose_name='Titre')
    description = models.TextField(max_length=2048, blank=True, verbose_name='Description')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, verbose_name='Image')
    time_created = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
    has_critique = models.BooleanField(default=False)
=======
>>>>>>> f3dc60dde3dd6edbe4a2fcebb4307cc0156b0a30

    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
<<<<<<< HEAD
        self.resize_image()
=======
        if self.image:
            self.resize_image()
>>>>>>> f3dc60dde3dd6edbe4a2fcebb4307cc0156b0a30


class Critique(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='Note')
    headline = models.CharField(max_length=128, verbose_name="Titre")
<<<<<<< HEAD
    body = models.TextField(max_length=8192, blank=True, verbose_name='Critique')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
=======
    body = models.CharField(max_length=8192, blank=True, verbose_name='Commentaire')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)


>>>>>>> f3dc60dde3dd6edbe4a2fcebb4307cc0156b0a30
