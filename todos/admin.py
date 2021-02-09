from django.contrib import admin
from .models import Todo, TodoPhoto

class TodoPhotoInline(admin.TabularInline):
    model = TodoPhoto

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    inlines = (TodoPhotoInline,)
    list_display = ('title', 'user', 'room', 'is_success')

    fieldsets = (
        (
           'Basic Info',
            {'fields':('title','user','room','description','start_date','end_date')}
        ),
    )


# Register your models here.
