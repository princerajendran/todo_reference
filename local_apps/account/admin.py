from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import AddUserForm, UpdateUserForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UpdateUserForm
    add_form = AddUserForm

    list_display = (
        'account_id', 'name', 'email', 'mobile', 'role', 'is_staff', 'date_joined')
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')
    readonly_fields = ['account_id', 'date_joined']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'date_joined')}),
        ('Personal info', {'fields': ('account_id', 'name', 'mobile', 'image', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'name', 'email', 'mobile', 'image', 'role', 'password1', 'password2'
                )
            }
        ),
    )
    search_fields = ('account_id', 'name', 'email', 'mobile')
    ordering = ("name", "email")
    filter_horizontal = ("groups", "user_permissions")
