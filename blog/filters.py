import django_filters

from blog.models.comment import Comment
from blog.models.post import Post


class CommentFilter(django_filters.FilterSet):
    is_changed = django_filters.BooleanFilter(field_name='is_changed', lookup_expr='exact')
    id = django_filters.NumberFilter(field_name="id", lookup_expr="exact")
    class Meta:
        model = Comment
        fields = ['id', 'is_changed', ]