from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),  # List and create posts
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),  # Retrieve, update, and delete a specific post
]
