from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("itemania.users.urls")),
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
