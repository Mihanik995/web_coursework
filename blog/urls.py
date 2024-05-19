from django.urls import path
from django.views.decorators.cache import cache_page

from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, post_delete
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', cache_page(300)(PostListView.as_view()), name='main'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='add_post'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', post_delete, name='delete_post'),
]
