from django.db import models

class Email(models.Model):
    email = models.EmailField(unique=True, max_length=254)

    def __str__(self):
        return str(self.email)
