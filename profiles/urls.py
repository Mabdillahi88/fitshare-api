from django.urls import path
from .views import ProfileList, ProfileDetail

urlpatterns = [
    path('', ProfileList.as_view(), name='profile-list'),  # List all profiles
    path('<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),  # Profile detail
]
