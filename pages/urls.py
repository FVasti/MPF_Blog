from django.urls import path
from .views import PostListView
from .views import PostDetailView
from .views import AboutView
from .views import PostCreateView
from .views import PostUpdateView
from .views import PostDeleteView

from . import views

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('posts/', views.posts_list, name='posts_list'),
]
