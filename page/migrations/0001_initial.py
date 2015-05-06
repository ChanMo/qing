# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Title')),
                ('description', models.TextField(verbose_name=b'Desc', blank=True)),
                ('content', ckeditor.fields.RichTextField(verbose_name=b'Content')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'Updated date')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'Updated date')),
                ('author', models.ForeignKey(related_name='Site', default=b'1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Name')),
                ('value', models.CharField(max_length=200, verbose_name=b'Value')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'Updated date')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'Updated date')),
            ],
        ),
        migrations.AddField(
            model_name='site',
            name='theme',
            field=models.ForeignKey(related_name='Site', default=b'1', verbose_name=b'Theme', to='page.Theme'),
        ),
        migrations.AddField(
            model_name='page',
            name='site',
            field=models.ForeignKey(related_name='Page', default=b'1', to='page.Site'),
        ),
        migrations.AddField(
            model_name='page',
            name='template',
            field=models.ForeignKey(related_name='Page', default=b'1', verbose_name=b'Tpl', to='page.Template'),
        ),
    ]
