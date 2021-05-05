from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UrlShortViewSet, url_redirect

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'urls', UrlShortViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('<str:url>/', url_redirect, name="redirect")
]
