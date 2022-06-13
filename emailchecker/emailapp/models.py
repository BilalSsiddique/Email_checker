from django.db import models

# Create your models here.
class email(models.Model):
    emal=models.EmailField(max_length=254)

    def __str__(self):
        return self.emal


