#!/home/chen/env/bin/python
# -*- coding: utf8 -*-

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=200, verbose_name='主题名称')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __unicode__(self):
        return self.name


class Template(models.Model):
    name = models.CharField(max_length=200, verbose_name='模板名称')
    value = models.CharField(max_length=200, verbose_name='模板值')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __unicode__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=200, verbose_name='站点名称')
    author = models.ForeignKey(User, related_name="站点", default='1')
    theme = models.ForeignKey(Theme, related_name="站点", default='1', verbose_name='主题')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __unicode__(self):
        return self.name

    def site_link(self):
        return '127.0.0.1:8000/m/'+str(self.id)


class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='文章标题')
    parent = models.ForeignKey('self', null=True, blank=True, default=None);
    site = models.ForeignKey(Site, related_name="文章", default='1')
    description = models.TextField(blank=True, verbose_name='描述')
    content = RichTextField(verbose_name='内容', config_name='awesome_ckeditor')
    template = models.ForeignKey(Template, related_name="文章", default='1', verbose_name='模板')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __unicode__(self):
        return self.title
