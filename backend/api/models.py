from django.db import models

# Create your models here.

class Messages(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Assuming you want to link to Django's built-in User model
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.message[:50]}..."  # Display first 50 characters of the message