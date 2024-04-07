from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    encrypted_password = models.CharField(max_length=255)

    class Meta:
        db_table = 'users'
