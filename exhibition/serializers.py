# coding: utf-8
from rest_framework import serializers, viewsets

from exhibition.models import CG, Anime, ShortVideo, Torrent


class CGSerializer(serializers.ModelSerializer):

    class Meta:
        model = CG
        exclude = ()


class CGViewset(viewsets.ModelViewSet):
    queryset = CG.objects.all()
    serializer_class = CGSerializer


class AnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anime
        exclude = ()


class AnimeViewset(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer


class TorrentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Torrent
        exclude = ()


class TorrentViewset(viewsets.ModelViewSet):
    queryset = Torrent.objects.all()
    serializer_class = TorrentSerializer


class ShortVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortVideo
        exclude = ()


class ShortVideoViewset(viewsets.ModelViewSet):
    queryset = ShortVideo.objects.all()
    serializer_class = ShortVideoSerializer
