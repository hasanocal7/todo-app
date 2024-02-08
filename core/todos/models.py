from django.db import models
from django.contrib.auth.models import User
from datetime import date

class UserProfile(models.Model):
    GENDER_CHOICES = {
        "M": "Male",
        "F": "Female"
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birthdate = models.DateField(default=date.today, blank=True, null=True)
    gender = models.CharField(max_length=1, choices = GENDER_CHOICES, default="M", blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Profiles'
    
class Todo(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="")
    isDone = models.BooleanField(default=False)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

