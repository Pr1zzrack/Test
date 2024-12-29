from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from config import settings
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/authentication/", include("apps.users.urls")),
    path("api/basket/", include("apps.cart.urls")),
    path("api/order/", include("apps.order.urls")),
    path("api/product/", include("apps.product_category.urls")),
    path("api/eye-test-signup/", include("apps.eye_test_signup.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/company_info/", include("apps.company_info.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
