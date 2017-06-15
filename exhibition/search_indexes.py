# -*- coding: utf-8 -*-
from haystack.indexes import SearchIndex, Indexable
from haystack.indexes import CharField, DateTimeField

from exhibition.models import Anime


class AnimeIndex(SearchIndex, Indexable):
    text = CharField(document=True)
    name = CharField(model_attr='name')
    orig_name = CharField(model_attr='orig_name', null=True)
    # pub_date = DateTimeField(model_attr='pub_date', null=True)

    def get_model(self):
        return Anime

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def prepare(self, obj):
        data = super(AnimeIndex, self).prepare(obj)
        data['text'] = data['name']
        return data
