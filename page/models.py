from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated date')

    def __unicode__(self):
        return self.name


class Template(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    value = models.CharField(max_length=200, verbose_name='Value')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated date')

    def __unicode__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    author = models.ForeignKey(User, related_name="Site", default='1')
    theme = models.ForeignKey(Theme, related_name="Site", default='1', verbose_name='Theme')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated date')

    def __unicode__(self):
        return self.name

    def site_link(self):
        return '127.0.0.1:8000/m/'+str(self.id)


class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    parent = models.ForeignKey('self', null=True, blank=True, default=None);
    site = models.ForeignKey(Site, related_name="Page", default='1')
    description = models.TextField(blank=True, verbose_name='Desc')
    content = RichTextField(verbose_name='Content', config_name='awesome_ckeditor')
    template = models.ForeignKey(Template, related_name="Page", default='1', verbose_name='Tpl')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated date')

    def __unicode__(self):
        return self.title
