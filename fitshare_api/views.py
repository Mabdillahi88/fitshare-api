from rest_framework.decorators import api_view
from rest_framework.response import Response

def home_view(request):
    return Response({"message": "Welcome to the FitShare API!"})

@api_view(['GET'])
def root_route(request):
    return Response({"message": "Welcome to the FitShare API root route!"})