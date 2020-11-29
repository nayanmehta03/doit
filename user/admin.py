from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import DoitUser
from personal.models import Board, Task


# Register your models here.

class DoitUserAdmin(UserAdmin):
    list_display = ('email', 'fullname', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'fullname',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'fullname', 'password', 'date_joined', 'last_login', 'is_admin', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'fullname', 'password', 'date_joined', 'last_login', 'is_admin', 'is_staff')}),
    )
    ordering = ('email',)


class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_of_creation', 'owner')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_of_creation', 'completed', 'ongoing', 'last_updated', 'board')


admin.site.register(DoitUser, DoitUserAdmin)
admin.site.unregister(Board)
admin.site.register(Board, BoardAdmin)
admin.site.unregister(Task)
admin.site.register(Task, TaskAdmin)
