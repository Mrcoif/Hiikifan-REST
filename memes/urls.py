from django.urls import path, include
from rest_framework import routers

from memes.views import MemeAPIList, MemeAPIUpdate, MemeAPIDestroy

# router = routers.DefaultRouter()
# router.register('', MemeViewSet, basename="memes")


urlpatterns = [
    # path('', include(router.urls)),
    path('', MemeAPIList.as_view()),
    path('<int:pk>/', MemeAPIUpdate.as_view()),
    path('<int:pk>/delete', MemeAPIDestroy.as_view()),
]
