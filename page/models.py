# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField

# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    value = models.CharField(max_length=200, verbose_name='Value')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __unicode__(self):
        return self.name


class Template(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    value = models.CharField(max_length=200, verbose_name='Value')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __unicode__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    author = models.ForeignKey(User, related_name="Site", default='1')
    theme = models.ForeignKey(Theme, related_name="Site", default='1', verbose_name='Theme')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __unicode__(self):
        return self.name

    def site_link(self):
        return '127.0.0.1:8000/m/'+str(self.id)


class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    parent = models.ForeignKey('self', null=True, blank=True, default=None);
    site = models.ForeignKey(Site, related_name="Page", default='1')
    icon = models.ImageField(upload_to='uploads/')
    color = ColorField()
    description = models.TextField(blank=True, verbose_name='Description')
    content = RichTextField(verbose_name='Content', config_name='awesome_ckeditor')
    template = models.ForeignKey(Template, related_name="Page", default='1', verbose_name='Template')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __unicode__(self):
        return self.title

    class Meta(object):
        ordering = ('order',)

    def icon_url(self):
        if self.icon:
            return u'<img src="%s" height="100">' % self.icon.url
        else:
            return ""

    icon_url.short_description = 'Thumb'
    icon_url.allow_tags = True
