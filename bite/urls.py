__author__ = "Shafikur Rahman"

from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.urls import users_router

router = DefaultRouter()

router.registry.extend(users_router.registry)

urlpatterns = [
    # api
    path("api/v1/", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
