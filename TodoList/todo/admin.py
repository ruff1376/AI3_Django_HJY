from django.contrib import admin

from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    # 할 일, 세부 내용, 상태, 작성된 날짜, 수정된 날짜 표시
    list_display = ('todo_title', 'todo_content', 'todo_status', 'todo_created_at', 'todo_updated_at')
    # 할 일, 세부 내용, 상태로 검색할 수 있는 검색 필드
    search_fields = ('title', 'content', 'status')

    def todo_title(self, obj):
        return obj.title
    
    def todo_content(self, obj):
        return obj.content
    
    def todo_status(self, obj):
        return obj.status
    
    # 날짜 포맷 : %Y-%m-%d %H:%M:%S
    def todo_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %H:%M:%S')
    
    def todo_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %H:%M:%S')
    
    # Admin 페이지의 Todo 컬럼명 지정
    todo_title.short_description = '할 일'
    todo_content.short_description = '세부 내용'
    todo_status.short_description = '상태'
    todo_created_at.short_description = '만든 날짜'
    todo_updated_at.short_description = '수정한 날짜'


admin.site.register(Todo, TodoAdmin)