from django.db import models
from django.contrib.auth.models import User

class Plainte(models.Model):
    CATEGORY_CHOICES = [
        ('route', 'Route endommagée'),
        ('eau', 'Coupure d\'eau'),
        ('eclairage', 'Problème d\'éclairage'),
        ('autre', 'Autre'),
    ]

    title = models.CharField(max_length=156)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associer le signalement à un utilisateur

    def __str__(self):
        return self.title
