from blog.models.comment import Comment
from blog.models.post import Post
from common.serializers.common import UserShortSerializer
from common.serializers.mixins import ExtendedModelSerializer


class CommentsShortSerializer(ExtendedModelSerializer):
    commentator = UserShortSerializer()

    class Meta:
        model = Comment
        fields = ('commentator',
                  'text',
                  'likes',
                  'is_changed',)


class PostShortSerializer(ExtendedModelSerializer):
    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  )


class PostSearchListSerializer(ExtendedModelSerializer):
    author = UserShortSerializer()
    comments = CommentsShortSerializer(many=True)

    class Meta:
        model = Post
        fields = ('author',
                  'comments',
                  'created_at',
                  'title',
                  'text',
                  'image',
                  'likes',
                  )


class PostListSerializer(ExtendedModelSerializer):
    author = UserShortSerializer()
    comments = CommentsShortSerializer(many=True)

    class Meta:
        model = Post
        fields = ('author',
                  'comments',
                  'created_at',
                  'title',
                  'text',
                  'image',
                  'likes',
                  )


class PostRetrieveSerializer(ExtendedModelSerializer):
    author = UserShortSerializer()
    comments = CommentsShortSerializer(many=True)

    class Meta:
        model = Post
        fields = ('author',
                  'comments',
                  'created_at',
                  'title',
                  'text',
                  'image',
                  'likes',
                  )


class PostCreateSerializer(ExtendedModelSerializer):
    author = UserShortSerializer()
    comments = CommentsShortSerializer(many=True)

    class Meta:
        model = Post
        fields = ('author',
                  'comments',
                  'created_at',
                  'title',
                  'text',
                  'image',
                  'likes',
                  )


class PostUpdateSerializer(ExtendedModelSerializer):
    author = UserShortSerializer()
    comments = CommentsShortSerializer(many=True)

    class Meta:
        model = Post
        fields = ('author',
                  'comments',
                  'created_at',
                  'title',
                  'text',
                  'image',
                  'likes',
                  )


class PostDeleteSerializer(ExtendedModelSerializer):
    author = UserShortSerializer()
    comments = CommentsShortSerializer(many=True)

    class Meta:
        model = Post
        fields = ('author',
                  'comments',
                  'created_at',
                  'title',
                  'text',
                  'image',
                  'likes',
                  )


class CommentSearchListSerializer(ExtendedModelSerializer):
    commentator = UserShortSerializer()
    post = PostShortSerializer()

    class Meta:
        model = Comment
        fields = ('id',
                  'created_at',
                  'text',
                  'likes',
                  'is_changed',
                  'commentator',
                  'post')


class CommentListSerializer(ExtendedModelSerializer):
    commentator = UserShortSerializer()
    post = PostShortSerializer()

    class Meta:
        model = Comment
        fields = ('id',
                  'created_at',
                  'text',
                  'likes',
                  'is_changed',
                  'commentator',
                  'post')


class CommentRetrieveSerializer(ExtendedModelSerializer):
    commentator = UserShortSerializer()
    post = PostShortSerializer()

    class Meta:
        model = Comment
        fields = ('id',
                  'created_at',
                  'text',
                  'likes',
                  'is_changed',
                  'commentator',
                  'post')


class CommentCreateSerializer(ExtendedModelSerializer):
    commentator = UserShortSerializer()
    post = PostShortSerializer()

    class Meta:
        model = Comment
        fields = ('id',
                  'created_at',
                  'text',
                  'likes',
                  'is_changed',
                  'commentator',
                  'post')


class CommentUpdateSerializer(ExtendedModelSerializer):
    commentator = UserShortSerializer()
    post = PostShortSerializer()

    class Meta:
        model = Comment
        fields = ('id',
                  'created_at',
                  'text',
                  'likes',
                  'is_changed',
                  'commentator',
                  'post')


class CommentDeleteSerializer(ExtendedModelSerializer):
    commentator = UserShortSerializer()
    post = PostShortSerializer()

    class Meta:
        model = Comment
        fields = ('id',
                  'created_at',
                  'text',
                  'likes',
                  'is_changed',
                  'commentator',
                  'post')