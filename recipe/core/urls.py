from django.contrib import admin
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'users/', include('authentication.urls')),
    re_path(r'api/', include('base.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
