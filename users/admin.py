from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from users.models.profile import Profile
from users.models.users import User


class ProfileAdmin(admin.StackedInline):
    model = Profile
    fields = (
            'telegram_id',
            'beans',
            'author_status',
            'liked_posts',
        )


@admin.register(User)
class UserAdmin(UserAdmin):
    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('username', 'phone_number', 'is_courier')}),
        (_('Личная информация'),
            {'fields': ('first_name', 'last_name', 'image')}),
        (_('Блог'),
            {'fields': ('subscriptions', 'subscribers',)}),
        (_('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', )}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldset = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'password1', 'password2', 'is_courier'),
        }),
    )
    list_display = ('id', 'full_name', 'email', 'phone_number', 'is_courier', )
    list_display_links = ('id', 'full_name', )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', )
    search_fields = ('first_name', 'last_name', 'id', 'email', 'phone_number', )
    ordering = ('id', )
    filter_horizontal = ('groups', 'user_permissions', )
    readonly_fields = ('last_login', )

    inlines = (ProfileAdmin, )
