from django.contrib import admin
from apps.master.models import Editor

# Register your models here.
class EditorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Editor, EditorAdmin)