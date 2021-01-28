from django.contrib import admin
from .models import Todo, TodoPhoto

class TodoPhotoInline(admin.TabularInline):
    model = TodoPhoto

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    inlines = (TodoPhotoInline,)
    list_display = ('title', 'user', 'room')

    fieldsets = (
        (
           'Basic Info',
            {'fields':('title','user','room','description',)}
        ),
    )


# Register your models here.
