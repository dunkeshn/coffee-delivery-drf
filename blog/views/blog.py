from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework.filters import SearchFilter, OrderingFilter

from blog.filters import CommentFilter
from blog.models.comment import Comment
from blog.models.post import Post
from blog.serializers.blog import PostSearchListSerializer, PostListSerializer, PostRetrieveSerializer, \
    PostCreateSerializer, PostUpdateSerializer, PostDeleteSerializer, CommentSearchListSerializer, \
    CommentListSerializer, CommentRetrieveSerializer, CommentCreateSerializer, CommentUpdateSerializer, \
    CommentDeleteSerializer
from common.views.mixins import ListViewSet, CRUDViewSet



# @extend_schema(
#     summary="Поиск статей",
#     tags=["Статьи"],
#     parameters=[
#         OpenApiParameter(name="title", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY,
#                          description="Поиск по названию статьи"),
#         OpenApiParameter(name="author", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY,
#                          description="Поиск по автору"),
#     ],
# )
@extend_schema_view(
    list=extend_schema(
        summary='Поиск статей',
        tags=['Статьи'],
        parameters=[
            # OpenApiParameter(
            #     name="id",
            #     type=OpenApiTypes.INT,
            #     location=OpenApiParameter.QUERY,
            #     description="Поиск по `id`"
            # ),
            OpenApiParameter(name="search", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY,
                             description="Поиск по `названию` и `тексту статьи`"),
            # OpenApiParameter(name="category", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY,
            #                  enum=[choice[0] for choice in Product.Category.choices],
            #                  description="Фильтр по `категории`"),
            OpenApiParameter(name="ordering", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY,
                             enum=["created_at", '-created_at' "likes", '-likes'],
                             description="Сортировка: `created_at` (по возрастанию), `-created_at` (по убыванию), `likes`, `-likes`"),
            OpenApiParameter(
                name="page",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="Количество страниц для пагинации"),
            OpenApiParameter(
                name="page_size",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="Количество элементов на одну страницу")
        ],
    )
)
class PostSearchView(ListViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSearchListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'text']
    ordering_fields = ['created_at', 'likes']


@extend_schema_view(
    list=extend_schema(summary="Список всех статей", tags=["Статьи"]),
    retrieve=extend_schema(summary="Детали статьи", tags=["Статьи"]),
    create=extend_schema(summary="Создать статью", tags=["Статьи"]),
    update=extend_schema(summary="Изменить статью", tags=["Статьи"]),
    partial_update=extend_schema(summary="Частично изменить статью", tags=["Статьи"]),
    destroy=extend_schema(summary="Удалить статью", tags=["Статьи"]),
)
class PostView(CRUDViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostRetrieveSerializer
        elif self.action == 'create':
            return PostCreateSerializer
        elif self.action == 'update':
            return PostUpdateSerializer
        elif self.action == 'partial_update':
            return PostUpdateSerializer
        elif self.action == 'destroy':
            return PostDeleteSerializer
        return self.serializer_class


@extend_schema_view(
    list=extend_schema(
        summary='Поиск комментариев',
        tags=['Комментарии'],
        parameters=[
            OpenApiParameter(
                name="id",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="Поиск по `id`"
            ),
            OpenApiParameter(name="search", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY,
                             description="Поиск по `тексту`, `автору комментария` и `названию статьи`"),
            OpenApiParameter(name="is_changed", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY,
                             enum=[False, True],
                             description="Изменен ли комментарий"),
            OpenApiParameter(name="ordering", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY,
                             enum=["created_at", '-created_at' "likes", '-likes'],
                             description="Сортировка: `created_at` (по возрастанию), `-created_at` (по убыванию), `likes`, `-likes`"),
            OpenApiParameter(
                name="page",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="Количество страниц для пагинации"),
            OpenApiParameter(
                name="page_size",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="Количество элементов на одну страницу")
        ],
    )
)
class CommentSearchView(ListViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSearchListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CommentFilter
    search_fields = ['id', 'commentator__username', 'post__title', ]
    ordering_fields = ['created_at', 'likes']


@extend_schema_view(
    list=extend_schema(summary="Список всех комментариев", tags=["Комментарии"]),
    retrieve=extend_schema(summary="Детали комментария", tags=["Комментарии"]),
    create=extend_schema(summary="Создать комментарий", tags=["Комментарии"]),
    update=extend_schema(summary="Изменить комментарий", tags=["Комментарии"]),
    partial_update=extend_schema(summary="Частично изменить комментарий", tags=["Комментарии"]),
    destroy=extend_schema(summary="Удалить комментарий", tags=["Комментарии"]),
)
class CommentView(CRUDViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CommentRetrieveSerializer
        elif self.action == 'create':
            return CommentCreateSerializer
        elif self.action == 'update':
            return CommentUpdateSerializer
        elif self.action == 'partial_update':
            return CommentUpdateSerializer
        elif self.action == 'destroy':
            return CommentDeleteSerializer
        return self.serializer_class