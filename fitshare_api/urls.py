from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Define a simple function-based view for the root URL
def home_view(request):
    return HttpResponse("Welcome to the FitShare API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Root URL will now display "Welcome to the FitShare API!"
    path('profiles/', include('profiles.urls')),  # Include profile URLs
    path('posts/', include('posts.urls')),  # Include posts URLs
    path('comments/', include('comments.urls')),  # Include comments URLs
    path('likes/', include('likes.urls')),  # Include likes URLs
    path('followers/', include('followers.urls')),  # Include followers URLs
    path('api-auth/', include('rest_framework.urls')),  # Added for login/logout in browsable API
    # JWT Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # dj-rest-auth endpoints
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  # Login, logout, password reset, etc.
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),  # Registration endpoint
]
