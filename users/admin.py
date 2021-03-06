from django.contrib import admin
from . import models

@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email',)
    fieldsets = ((
        'bananana',{'fields':('email','nickname','photo')}
                 ),
    )
# Register your models here.
