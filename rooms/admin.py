from django.contrib import admin
from . import models

# Register your models here.
class RoomPhotoInline(admin.TabularInline):
    model = models.RoomPhoto

@admin.register(models.Room)
class CustomRoomAdmin(admin.ModelAdmin):
    inlines = (RoomPhotoInline,)
    list_display = ('title', 'description', 'host')
    fieldsets = ((
        'Basic Info', {'fields': ('title', 'description', 'host')},
                 ),
    )


