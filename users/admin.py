from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     model = CustomUser

#     # fieldsets = UserAdmin.fieldsets + (
#     #     (None, {'fields': ('email',)}),
#     # )
#     add_fieldsets = ((None, {'classes': ('wide',), 'fields': ('username', 'email', 'password1', 'password2'),},),)
#     list_display = ('username', 'email', 'is_staff', 'is_active')
#     search_fields = ('username', 'email')
#     ordering = ('username',)

# admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(CustomUser, UserAdmin)
