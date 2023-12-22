from django.contrib import admin
from user.models import UserAccount

# Register your models here.

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name", "father_name", "is_active", "img_preview"]
    search_fields = ["email", "first_name", "last_name"]
    list_filter =["is_active"]
