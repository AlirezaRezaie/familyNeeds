from django.conf.urls import include
from django.contrib import admin
from .views import login_page, main_router
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("needs/", include('needs.urls')),
    path("login/", login_page),
    path("", main_router)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
