from django.contrib import admin

from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('todo_title', 'todo_content', 'todo_status', 'todo_created_at', 'todo_updated_at')
    search_fields = ('title', 'content', 'status')

    def todo_title(self, obj):
        return obj.title
    
    def todo_content(self, obj):
        return obj.content
    
    def todo_status(self, obj):
        return obj.status
    
    def todo_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %H:%M:%S')
    
    def todo_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %H:%M:%S')
    
    todo_title.short_description = '할 일'
    todo_content.short_description = '세부 내용'
    todo_status.short_description = '상태'
    todo_created_at.short_description = '작성된 날짜'
    todo_updated_at.short_description = '수정된 날짜'


admin.site.register(Todo, TodoAdmin)