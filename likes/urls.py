from django.urls import path
from .views import LikeList

urlpatterns = [
    path('', LikeList.as_view(), name='like-list'),
]
