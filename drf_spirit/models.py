# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from autoslug import AutoSlugField
from django.db import models
from django.db.models import F
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone

from .config import COMMENT_ACTION, COMMENT


class Category(models.Model):
    """
    Category model
    """
    parent = models.ForeignKey('self', verbose_name=_("category parent"), blank=True, null=True)

    title = models.CharField(_("title"), max_length=75)
    slug = AutoSlugField(populate_from="title", blank=True, unique=True)
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

    def __unicode__(self):
        return self.title.encode('utf-8')

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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='spirit_topics', editable=False)
    category = models.ForeignKey(Category, verbose_name=_("category"))

    title = models.CharField(_("title"), max_length=255)
    slug = AutoSlugField(populate_from="title", blank=True, unique=True)
    date = models.DateTimeField(_("date"), default=timezone.now, blank=True, editable=False)
    last_active = models.DateTimeField(_("last active"), default=timezone.now, blank=True, editable=False)

    is_pinned = models.BooleanField(_("pinned"), default=False, editable=False)
    is_globally_pinned = models.BooleanField(_("globally pinned"), default=False, editable=False)
    is_closed = models.BooleanField(_("closed"), default=False)
    is_removed = models.BooleanField(default=False)

    view_count = models.PositiveIntegerField(_("views count"), default=0, editable=False)
    comment_count = models.PositiveIntegerField(_("comment count"), default=0, editable=False)

    class Meta:
        ordering = ['-last_active', '-pk']
        verbose_name = _("topic")
        verbose_name_plural = _("topics")

    def __unicode__(self):
        return self.title.encode('utf-8')

    def get_absolute_url(self):
        return reverse('drf_spirit:topic-detail', kwargs={'pk': str(self.id), 'slug': self.slug})

    @property
    def main_category(self):
        return self.category.parent or self.category

    def increase_view_count(self):
        Topic.objects.filter(pk=self.pk).update(view_count=F('view_count') + 1)

    def increase_comment_count(self):
        Topic.objects.filter(pk=self.pk).update(comment_count=F('comment_count') + 1, last_active=timezone.now())

    def decrease_comment_count(self):
        # todo: update last_active to last() comment
        Topic.objects.filter(pk=self.pk).update(comment_count=F('comment_count') - 1)


class Comment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='forum_comments', editable=False)
    topic = models.ForeignKey(Topic, related_name='comments')

    comment = models.TextField(_("comment"))
    action = models.IntegerField(_("action"), choices=COMMENT_ACTION, default=COMMENT)
    date = models.DateTimeField(default=timezone.now, blank=True, editable=False)
    is_removed = models.BooleanField(default=False)
    is_modified = models.BooleanField(default=False, editable=False)
    ip_address = models.GenericIPAddressField(blank=True, null=True, editable=False)

    modified_count = models.PositiveIntegerField(_("modified count"), default=0, editable=False)
    likes_count = models.PositiveIntegerField(_("likes count"), default=0, editable=False)

    class Meta:
        ordering = ['-date', '-pk']
        verbose_name = _("comment")
        verbose_name_plural = _("comments")

    def __unicode__(self):
        return self.comment[:10].encode('utf-8')

    def increase_modified_count(self):
        Comment.objects.filter(pk=self.pk).update(modified_count=F('modified_count') + 1)

    def increase_likes_count(self):
        Comment.objects.filter(pk=self.pk).update(likes_count=F('likes_count') + 1)

    def decrease_likes_count(self):
        (Comment.objects.filter(pk=self.pk, likes_count__gt=0)
                        .update(likes_count=F('likes_count') - 1))
