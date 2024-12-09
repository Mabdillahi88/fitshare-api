from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from fitshare_api.views import root_route, logout_view  # Imported root_route and logout_view

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('', root_route, name='root'),  # Root URL for the API
    path('logout/', logout_view, name='logout'),  # Added custom logout route
    path('profiles/', include('profiles.urls')),  # Profile-related URLs
    path('posts/', include('posts.urls')),  # Post-related URLs
    path('comments/', include('comments.urls')),  # Comment-related URLs
    path('likes/', include('likes.urls')),  # Like-related URLs
    path('followers/', include('followers.urls')),  # Follower-related URLs
    path('api-auth/', include('rest_framework.urls')),  # Browsable API login/logout
    # JWT Endpoints for authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # dj-rest-auth endpoints
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  # Authentication-related URLs
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),  # User registration-related URLs
]
