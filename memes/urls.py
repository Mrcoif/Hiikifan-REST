from django.urls import path, include
from rest_framework import routers
from .views import MemeViewSet


router = routers.DefaultRouter()
router.register(r'', MemeViewSet, basename='memes')
print(router.urls)

urlpatterns = [
    path('', include(router.urls)),
]
