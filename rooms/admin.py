from django.contrib import admin
from . import models

@admin.register(models.Room)
class CustomRoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'host')
    fieldsets = ((
        'Basic Info', {'fields': ('title', 'description', 'host', 'participants')},
                 ),
                 (
         'Photo', {'fields': ('photo', 'photo_caption')}
                 ),
    )


