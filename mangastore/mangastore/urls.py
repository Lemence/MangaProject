from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from manga.views import MangaViewSet

router = routers.DefaultRouter()
router.register(r'manga', MangaViewSet, basename='Manga')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
