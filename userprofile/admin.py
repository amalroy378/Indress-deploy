from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Account,Address,User_Profile

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'username')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account,AccountAdmin)
admin.site.register(Address)
admin.site.register(User_Profile)