# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from autoslug import AutoSlugField
from django.db import models
from django.db.models import F
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    """
    Category model
    """
    parent = models.ForeignKey('self', verbose_name=_("category parent"), null=True)

    title = models.CharField(_("title"), max_length=75)
    slug = AutoSlugField(populate_from="title", db_index=False, blank=True)
    description = models.CharField(_("description"), max_length=255, blank=True)
    color = models.CharField(_("color"), max_length=7, blank=True,
                             help_text=_("Title color in hex format (i.e: #1aafd0)."))

    is_global = models.BooleanField(_("global"), default=True,
                                    help_text=_('Designates whether the topics will be'
                                                'displayed in the all-categories list.'))
    is_closed = models.BooleanField(_("closed"), default=False)
    is_removed = models.BooleanField(_("removed"), default=False)
    is_private = models.BooleanField(_("private"), default=False)

    class Meta:
        ordering = ['-pk']
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def get_absolute_url(self):
        return reverse(
                'drf_spirit:category-detail',
                kwargs={'pk': str(self.id), 'slug': self.slug})

    @property
    def is_subcategory(self):
        if self.parent_id:
            return True
        else:
            return False


class Topic(models.Model):
    """
    Topic model
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='spirit_topics')
    category = models.ForeignKey(Category, verbose_name=_("category"))

    title = models.CharField(_("title"), max_length=255)
    slug = AutoSlugField(populate_from="title", db_index=True, blank=True)
    date = models.DateTimeField(_("date"), default=timezone.now)
    last_active = models.DateTimeField(_("last active"), default=timezone.now)

    is_pinned = models.BooleanField(_("pinned"), default=False)
    is_globally_pinned = models.BooleanField(_("globally pinned"), default=False)
    is_closed = models.BooleanField(_("closed"), default=False)
    is_removed = models.BooleanField(default=False)

    view_count = models.PositiveIntegerField(_("views count"), default=0)
    comment_count = models.PositiveIntegerField(_("comment count"), default=0)


    class Meta:
        ordering = ['-last_active', '-pk']
        verbose_name = _("topic")
        verbose_name_plural = _("topics")

    def get_absolute_url(self):
        return reverse('drf_spirit:topic-detail', kwargs={'pk': str(self.id), 'slug': self.slug})

    @property
    def main_category(self):
        return self.category.parent or self.category

    @property
    def is_visited(self):
        return bool(self.bookmark)

    def increase_view_count(self):
        Topic.objects\
            .filter(pk=self.pk)\
            .update(view_count=F('view_count') + 1)

    def increase_comment_count(self):
        Topic.objects\
            .filter(pk=self.pk)\
            .update(comment_count=F('comment_count') + 1, last_active=timezone.now())

    def decrease_comment_count(self):
        # todo: update last_active to last() comment
        Topic.objects\
            .filter(pk=self.pk)\
            .update(comment_count=F('comment_count') - 1)
