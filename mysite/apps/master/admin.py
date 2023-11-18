from typing import Any
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib import messages
from apps.master.models import Editor

# Register your models here.
class EditorAdmin(UserAdmin):
    list_display = ('email', 'name', 'is_staff', 'is_superuser')
    search_fields = ('email', 'name')
    ordering = ('email',)
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    
    def save_model(self, request: Any, obj: Any, form: Any, change: Any):
        obj.save()
        messages.add_message(request,level = messages.SUCCESS, message = "Add Account Success")
admin.site.register(Editor, EditorAdmin)