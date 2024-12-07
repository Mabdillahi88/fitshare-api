from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

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
]
