from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

def home_view(request):
    return Response({"message": "Welcome to the FitShare API!"})

@api_view(['GET'])
def root_route(request):
    return Response({"message": "Welcome to the FitShare API root route!"})

@api_view(['POST'])
def logout_view(request):
    """
    Custom logout view to fix the dj-rest-auth logout bug.
    This ensures the JWT cookies are properly cleared.
    """
    response = Response({"detail": "Successfully logged out."})
    response.delete_cookie(settings.JWT_AUTH_COOKIE, samesite=settings.JWT_AUTH_SAMESITE, secure=True, httponly=True)
    response.delete_cookie(settings.JWT_AUTH_REFRESH_COOKIE, samesite=settings.JWT_AUTH_SAMESITE, secure=True, httponly=True)
    return response
