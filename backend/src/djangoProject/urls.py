from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title="ТехноЦех",
        default_version='v1',
        description="Cистема менеджмента проектов",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('worker_shifts.api.v1.urls')),  # Ensure this line is added
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/account/', include('account.api.v1.urls')),  # Include account app URLs here

]
