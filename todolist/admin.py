from django.contrib import admin

# Register your models here.
from .models import Category, Status, Task


class taskColumn(admin.ModelAdmin):
    list_display = ['category_id', 'status_id', 'title', 'description',
                    'due_date']
    search_fields = ['title']
    list_filter = ('category_id', 'status_id',)
    list_per_page = 10


admin.site.register(Task, taskColumn)
admin.site.register(Category)
admin.site.register(Status)
