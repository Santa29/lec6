from django.urls import path 

from .views import PostListView, PostUpdateView, PostDeleteView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path("new/", PostCreateView.as_view(), name = 'post_new'),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]