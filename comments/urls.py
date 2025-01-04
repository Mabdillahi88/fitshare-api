from django.urls import path
from .views import CommentList, CommentDetail

urlpatterns = [
    path('', CommentList.as_view(), name='comment-list'),  # List and create comments
    path('<int:pk>/', CommentDetail.as_view(), name='comment-detail'),  # Retrieve, update, and delete a specific comment
]
