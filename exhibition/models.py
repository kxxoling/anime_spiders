# coding: utf-8
from django.db.models import Model as _Model
from django.db.models import ForeignKey
from django.db.models import CharField, IntegerField, DateTimeField

from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase


class Tag(TagBase):
    desc = CharField(max_length=300, null=True, default=None)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Tagged(GenericTaggedItemBase):
    tag = ForeignKey(Tag, related_name='%(app_label)s_%(class)s_items')


class Model(_Model):
    class Meta:
        abstract = True
        unique_together = (
            ('crawled_from', 'site_pk'),
        )
    crawled_from = CharField(max_length=100)
    site_pk = IntegerField()
    tags = TaggableManager(through=Tagged)

    def __unicode__(self):
        return u'<%s: %s from %s>' % (
            self.__class__.__name__, self.site_pk, self.crawled_from)


class Torrent(Model):

    site = CharField(max_length=30)
    title = CharField(max_length=100)
    team_name = CharField(max_length=100, null=True)
    team_id = IntegerField(null=True)
    size = IntegerField(null=True)
    torrent = CharField(max_length=100, null=True)
    magnet = CharField(max_length=300)
    link = CharField(max_length=200)
    pub_date = DateTimeField(null=True)
    author = CharField(max_length=50)
    category = CharField(max_length=50)

    torrent_path = CharField(max_length=100, null=True)

    def __unicode__(self):
        return '%s - %s' % (super(Torrent, self).__unicode__(), self.title)


class CG(Model):

    large_file_url = CharField(max_length=100)
    file_url = CharField(max_length=100)
    source = CharField(max_length=300)
    tags_string = CharField(max_length=100)
    md5 = CharField(max_length=100)
    pixiv_id = IntegerField(null=True)


class Anime(Model):

    link = CharField(max_length=100)
    cover = CharField(max_length=100, null=True)
    name = CharField(max_length=100)
    orig_name = CharField(max_length=100, null=True)
    pub_date = CharField(max_length=100)

    cover_path = CharField(max_length=100, null=True)


class ShortVideo(Model):

    md5 = CharField(max_length=100)
    preview_url = CharField(max_length=100)
    file_url = CharField(max_length=100)
    file_size = IntegerField()
    author = CharField(max_length=100)
    source = CharField(max_length=100)
    score = IntegerField()
    file_ext = CharField(max_length=10)

    file_path = CharField(max_length=100, null=True)
    preview_path = CharField(max_length=100, null=True)
