# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 11:09
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drf_spirit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='comment')),
                ('action', models.IntegerField(choices=[(0, 'comment'), (1, 'topic moved'), (2, 'topic closed'), (3, 'topic unclosed'), (4, 'topic pinned'), (5, 'topic unpinned')], default=0, verbose_name='action')),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('is_removed', models.BooleanField(default=False)),
                ('is_modified', models.BooleanField(default=False)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('modified_count', models.PositiveIntegerField(default=0, verbose_name='modified count')),
                ('likes_count', models.PositiveIntegerField(default=0, verbose_name='likes count')),
            ],
            options={
                'ordering': ['-date', '-pk'],
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='last_active',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='last active'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='drf_spirit.Topic'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
