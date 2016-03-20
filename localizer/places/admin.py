from django.contrib import admin

from .models import Place, Photo, Types

admin.site.register(Place)
admin.site.register(Photo)
admin.site.register(Types)