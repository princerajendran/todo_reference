from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('local_apps.account.urls')),
    path('api/main/', include('local_apps.main.urls')),
    path('api/tasks/', include('local_apps.tasks.urls')),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
    re_path('assets/media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path('assets/static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
