from django.contrib import admin

from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'status')

admin.site.register(Todo, TodoAdmin)