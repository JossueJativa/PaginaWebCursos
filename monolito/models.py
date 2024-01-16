from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Cursos(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='cursos/images')
    precio = models.FloatField()

    def photo_url(self):
        if self.image:
            return self.image.url
        return None
    
class User(AbstractUser):
    cursos = models.ManyToManyField(Cursos, related_name='cursos')