from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("itemania.users.urls")),
    path("api/", include("itemania.items.urls")),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

if settings.DEBUG:
    if "silk" in settings.INSTALLED_APPS:
        urlpatterns += [
            path(
                "__debug__/",
                include(
                    "silk.urls",
                    namespace="silk",
                ),
            ),
        ]
