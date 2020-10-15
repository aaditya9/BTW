from django.contrib import admin
from btwapps.accounts.models.User import User
from btwapps.accounts.models.Profile import Profile

# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
