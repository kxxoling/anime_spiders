# coding: utf-8
from django.contrib import admin
from exhibition.models import Torrent, CG, ShortVideo, Anime


admin.site.register(Torrent)
admin.site.register(CG)
admin.site.register(ShortVideo)
admin.site.register(Anime)
