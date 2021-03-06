# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-15 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('exhibition', '0003_add_taggs_20170612_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaggedActs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedacts_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedacts_TaggedActs', to='exhibition.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedAnimeDirectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedanimedirectors_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedanimedirectors_TaggedAnimeDirectors', to='exhibition.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedAssitCompanies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedassitcompanies_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedassitcompanies_TaggedAssitCompanies', to='exhibition.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedAudioDirectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedaudiodirectors_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedaudiodirectors_TaggedAudioDirectors', to='exhibition.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedCharactorDesigners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedcharactordesigners_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedcharactordesigners_TaggedCharactorDesigners', to='exhibition.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedcompany_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedcompany_companies', to='exhibition.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedDirectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggeddirectors_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggeddirectors_TaggedDirectors', to='exhibition.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedEffectMakers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedeffectmakers_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedeffectmakers_TaggedEffectMakers', to='exhibition.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedMainAnimators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedmainanimators_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedmainanimators_TaggedMainAnimators', to='exhibition.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedMechanicalDesigners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedmechanicaldesigners_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedmechanicaldesigners_TaggedMechanicalDesigners', to='exhibition.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedMusicians',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedmusicians_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedmusicians_TaggedMusicians', to='exhibition.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedPhotoDirectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedphotodirectors_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedphotodirectors_TaggedPhotoDirectors', to='exhibition.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedScenarists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedscenarists_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedscenarists_TaggedScenarists', to='exhibition.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedStoryboardDirectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedstoryboarddirectors_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibition_taggedstoryboarddirectors_TaggedStoryboardDirectors', to='exhibition.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='anime',
            name='alter_names',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='anime',
            name='company',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='exhibition.Tag'),
        ),
        migrations.AddField(
            model_name='anime',
            name='episodes',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.Tagged', to='exhibition.Tag', verbose_name=b'tags'),
        ),
        migrations.AlterField(
            model_name='cg',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.Tagged', to='exhibition.Tag', verbose_name=b'tags'),
        ),
        migrations.AlterField(
            model_name='shortvideo',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.Tagged', to='exhibition.Tag', verbose_name=b'tags'),
        ),
        migrations.AlterField(
            model_name='torrent',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.Tagged', to='exhibition.Tag', verbose_name=b'tags'),
        ),
        migrations.AddField(
            model_name='anime',
            name='acts',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.TaggedActs', to='exhibition.Tag', verbose_name='\u6f14\u51fa'),
        ),
        migrations.AddField(
            model_name='anime',
            name='anime_directors',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.TaggedAnimeDirectors', to='exhibition.Tag', verbose_name='\u4f5c\u753b\u76d1\u7763'),
        ),
        migrations.AddField(
            model_name='anime',
            name='assit_companies',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.TaggedAssitCompanies', to='exhibition.Tag', verbose_name='\u534f\u529b\u5236\u4f5c'),
        ),
        migrations.AddField(
            model_name='anime',
            name='audio_directors',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.TaggedAudioDirectors', to='exhibition.Tag', verbose_name='\u97f3\u54cd\u76d1\u7763'),
        ),
        migrations.AddField(
            model_name='anime',
            name='charactor_designers',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.TaggedCharactorDesigners', to='exhibition.Tag', verbose_name='\u4eba\u7269\u8bbe\u8ba1'),
        ),
        migrations.AddField(
            model_name='anime',
            name='directors',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.TaggedDirectors', to='exhibition.Tag', verbose_name='\u52a8\u753b\u76d1\u7763'),
        ),
        migrations.AddField(
            model_name='anime',
            name='effect_makers',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.TaggedEffectMakers', to='exhibition.Tag', verbose_name='\u7279\u6548\u5e08'),
        ),
        migrations.AddField(
            model_name='anime',
            name='main_animators',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.TaggedMainAnimators', to='exhibition.Tag', verbose_name='\u539f\u753b'),
        ),
        migrations.AddField(
            model_name='anime',
            name='mechanical_designers',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.TaggedMechanicalDesigners', to='exhibition.Tag', verbose_name='\u673a\u68b0\u8bbe\u8ba1'),
        ),
        migrations.AddField(
            model_name='anime',
            name='musicians',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.TaggedMusicians', to='exhibition.Tag', verbose_name='\u97f3\u4e50'),
        ),
        migrations.AddField(
            model_name='anime',
            name='photo_directors',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.TaggedPhotoDirectors', to='exhibition.Tag', verbose_name='\u6444\u5f71\u76d1\u7763'),
        ),
        migrations.AddField(
            model_name='anime',
            name='scenarists',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.TaggedScenarists', to='exhibition.Tag', verbose_name='\u811a\u672c'),
        ),
        migrations.AddField(
            model_name='anime',
            name='storyboard_directors',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.TaggedStoryboardDirectors', to='exhibition.Tag', verbose_name='\u5206\u955c'),
        ),
    ]
