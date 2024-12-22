from django.contrib import admin
from django.urls import path, include
from fitshare_api.views import root_route, logout_route

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_route, name='root'),
    path('dj-rest-auth/logout/', logout_route),  # Updated to match drf_api
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('profiles/', include('profiles.urls')),
    path('posts/', include('posts.urls')),
    path('comments/', include('comments.urls')),
    path('likes/', include('likes.urls')),
    path('followers/', include('followers.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
