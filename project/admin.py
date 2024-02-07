from django.contrib import admin

# Register your models here.
from .models import (
    Tutorial,
    Video
)
admin.site.register(Tutorial)
admin.site.register(Video)
