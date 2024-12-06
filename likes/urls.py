from django.urls import path
from .views import LikeList, LikeDetail

urlpatterns = [
    path('', LikeList.as_view(), name='like-list'),
    path('<int:pk>/', LikeDetail.as_view(), name='like-detail'),
]
