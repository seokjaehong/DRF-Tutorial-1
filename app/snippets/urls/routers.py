from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ..apis.viewsets import SnippetViewSet

router = DefaultRouter()
router.register(r'', SnippetViewSet)

urlpatterns = [
    path('', include(router.urls))
]
