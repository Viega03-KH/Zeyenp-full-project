from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', include('gallery_app.urls')),
    path('', include('home_app.urls')),
    path('', include('news_app.urls')),
]

urlpatterns += i18n_patterns(
    path('', include('gallery_app.urls')),
    path('', include('home_app.urls')),
    path('', include('news_app.urls')),
)

# Statik va media fayllar
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)