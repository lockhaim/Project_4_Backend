from django.contrib import admin

# Register your models here.
from .models import Guide
from .models import User
admin.site.register(Guide)
admin.site.register(User)
