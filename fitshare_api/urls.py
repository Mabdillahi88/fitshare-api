from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from fitshare_api.views import root_route, logout_view

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),
    
    # Root route
    path('', root_route, name='root'),
    
    # Custom logout route
    path('logout/', logout_view, name='logout'),
    
    # Application-specific URLs
    path('profiles/', include('profiles.urls')),  # Profiles app
    path('posts/', include('posts.urls')),        # Posts app
    path('comments/', include('comments.urls')),  # Comments app
    path('likes/', include('likes.urls')),        # Likes app
    path('followers/', include('followers.urls')),  # Followers app
    
    # Browsable API login/logout
    path('api-auth/', include('rest_framework.urls')),
    
    # JWT token authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # dj-rest-auth endpoints
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  # Authentication
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),  # Registration
]
