from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html
from blog.models.post import Post
from blog.models.comment import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name_link', 'likes', 'created_at', 'is_changed', )
    list_display_links = ('id', 'full_name_link')
    list_filter = ('is_changed',)
    search_fields = ('text', 'commentator__first_name', 'commentator__last_name', 'commentator__username', )
    readonly_fields = (
        'created_at', 'updated_at',
    )

    def full_name_link(self, obj):
        link = reverse('admin:users_user_change', args=[obj.commentator.id])
        return format_html('<a href="{}">{}</a>', link, f'{obj.commentator.first_name} {obj.commentator.last_name}')
    full_name_link.short_description = 'Имя пользователя'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name_link', 'title', 'likes',  'created_at', 'comments_count', )
    list_display_links = ('id', 'full_name_link', 'title', )
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('text', 'title', 'author__first_name', 'author__last_name', 'author__username', )

    def full_name_link(self, obj):
        link = reverse('admin:users_user_change', args=[obj.author.id])
        return format_html('<a href="{}">{}</a>', link, f'{obj.author.first_name} {obj.author.last_name}')
    full_name_link.short_description = 'Имя пользователя'

    def comments_count(self, obj):
        return obj.comments_count
    comments_count.short_description = 'Количество комментариев'

    def get_queryset(self, request):
        queryset = super().get_queryset(request).annotate(comments_count=Count('comments'))
        return queryset
