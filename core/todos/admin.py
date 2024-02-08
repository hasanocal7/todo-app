from django.contrib import admin
from .models import UserProfile, Todo

admin.site.register(UserProfile)
admin.site.register(Todo)