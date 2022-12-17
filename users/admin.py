from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    readonly_fields = ("date_joined", "last_login")

    fieldsets = (
        ("Credenciais", {"fields": ("username", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "account_balance",
                    "favorite_color",
                    "is_married",
                    "children",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_superuser")}),
        ("Dates", {"fields": ("last_login", "date_joined")}),)

admin.site.register(User, CustomUserAdmin)
