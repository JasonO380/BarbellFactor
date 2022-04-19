from django.contrib import admin

# Register your models here.
from .models import Video
admin.site.register(Video)
from .models import User
admin.site.register(User)