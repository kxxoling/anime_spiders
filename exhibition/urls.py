"""exhibition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from rest_framework import routers

import exhibition.admins  # noqa
from exhibition.serializers import CGViewset, AnimeViewset,\
    ShortVideoViewset, TorrentViewset


router = routers.DefaultRouter()
router.register(r'cgs', CGViewset)
router.register(r'animes', AnimeViewset)
router.register(r'shortvideos', ShortVideoViewset)
router.register(r'torrents', TorrentViewset)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]

urlpatterns += static(
    '^storage/', document_root=os.path.join(settings.BASE_DIR, '.storage')
    )
