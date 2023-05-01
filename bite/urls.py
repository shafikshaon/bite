__author__ = "Shafikur Rahman"

import rest_framework_simplejwt
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.urls import users_router

schema_view = get_schema_view(
    openapi.Info(
        title="Bite API",
        default_version="v1",
        description="",
        terms_of_service="",
        contact=openapi.Contact(email="shafikshaon@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    authentication_classes=(rest_framework_simplejwt.authentication.JWTAuthentication,),
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

router.registry.extend(users_router.registry)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("health/", include("health_check.urls")),
    # swagger docs
    path("swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
