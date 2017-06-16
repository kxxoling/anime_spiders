# coding: utf-8
from django.db.models import Model as _Model
from django.db.models import ForeignKey
from django.db.models import CharField, IntegerField, DateTimeField, TextField

from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase


class Tag(TagBase):
    desc = CharField(max_length=300, null=True, default=None)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Tagged(GenericTaggedItemBase):
    tag = ForeignKey(Tag, related_name='%(app_label)s_%(class)s_items')


class TaggedCompany(GenericTaggedItemBase):
    tag = ForeignKey(Tag, related_name='%(app_label)s_%(class)s_companies')


def camel_case(s):
    words = s.split('_')
    return ''.join(map(
        lambda s: s.capitalize(),
        words))


def tagged_as(name, verbose_name=None):
    name = 'Tagged' + camel_case(name)
    _tagged = type(name, (GenericTaggedItemBase,), {
        'tag': ForeignKey(Tag, related_name='%(app_label)s_%(class)s_'+name),
        '__module__': 'exhibition.models',
    })

    manager = TaggableManager(through=_tagged, verbose_name=verbose_name or name)
    manager.rel.related_name = "+"
    return manager
    # return TaggableManager(through=_tagged, verbose_name=verbose_name or name)


class Model(_Model):
    class Meta:
        abstract = True
        unique_together = (
            ('crawled_from', 'site_pk'),
        )
    crawled_from = CharField(max_length=100)
    site_pk = IntegerField()
    tags = TaggableManager(through=Tagged, verbose_name='tags')

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

    episode_length = IntegerField(null=True, default=None)
    alter_names = CharField(max_length=100, null=True, default=None)

    company = ForeignKey(Tag, related_name='companies', null=True, default=None)
    assit_companies = tagged_as('assit_companies', verbose_name=u'协力制作')

    directors = tagged_as('directors', verbose_name=u'动画监督')
    scenarists = tagged_as('scenarists', verbose_name=u'脚本')
    effect_makers = tagged_as('effect_makers', verbose_name=u'特效师')
    audio_directors = tagged_as('audio_directors', verbose_name=u'音响监督')
    main_animators = tagged_as('main_animators', verbose_name=u'原画')
    photo_directors = tagged_as('photo_directors', verbose_name=u'摄影监督')
    mechanical_designers = tagged_as('mechanical_designers', verbose_name=u'机械设计')
    anime_directors = tagged_as('anime_directors', verbose_name=u'作画监督')
    charactor_designers = tagged_as('charactor_designers', verbose_name=u'人物设计')
    storyboard_directors = tagged_as('storyboard_directors', verbose_name=u'分镜')
    acts = tagged_as('acts', verbose_name=u'演出')

    musicians = tagged_as('musicians', verbose_name=u'音乐')

    desc = TextField(null=False, blank=True, default='')
    episodes = TextField(null=True, default=None)

    def __unicode__(self):
        return u'<%s: %s from %s>' % (
            self.__class__.__name__, self.name, self.crawled_from)


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
