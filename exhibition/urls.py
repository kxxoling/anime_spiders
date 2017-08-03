# coding: utf-8
import os

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from rest_framework import routers

import exhibition.admins  # noqa
from exhibition import views
from exhibition.serializers import CGViewset, AnimeViewset,\
    ShortVideoViewset, TorrentViewset


router = routers.DefaultRouter()
router.register(r'cgs', CGViewset)
router.register(r'animes', AnimeViewset)
router.register(r'shortvideos', ShortVideoViewset)
router.register(r'torrents', TorrentViewset)


urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]

urlpatterns += static(
    'storage/', document_root=os.path.join(settings.BASE_DIR, '.storage')
    )
