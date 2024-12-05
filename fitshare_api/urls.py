from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Define a simple function-based view for the root URL
def home_view(request):
    return HttpResponse("Welcome to the FitShare API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Root URL will now display "Welcome to the FitShare API!"
    path('profiles/', include('profiles.urls')),
]
