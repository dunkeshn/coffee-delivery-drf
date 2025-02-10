from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.views.blog import PostSearchView, PostView, CommentView, CommentSearchView

router = DefaultRouter()

router.register(r'post/search', PostSearchView, 'post_search')
router.register(r'post/manage', PostView, 'post_manage')
router.register(r'comment/search', CommentSearchView, 'comment_search')
router.register(r'comment/manage', CommentView, 'comment_manage')



urlpatterns = [

]

urlpatterns += path('blog/', include(router.urls)),