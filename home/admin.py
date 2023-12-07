from django.contrib import admin
from .models import Task, Tag

class TaskAdmin(admin.ModelAdmin):
    list_display = ('tasktitle', 'taskDesc', 'time', 'due_date', 'status')
    search_fields = ('tasktitle', 'taskDesc', 'status')
    list_filter = ('status', 'tags')

    fieldsets = (
        ('Task Information', {
            'fields': ('tasktitle', 'taskDesc', 'status', 'tags')
        }),
        ('Time Information', {
            'fields': ('time',),
            'classes': ('collapse',),
        }),
        ('Due Date', {
            'fields': ('due_date',),
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['time']
        else:
            return []

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Task, TaskAdmin)
admin.site.register(Tag, TagAdmin)
