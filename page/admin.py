from django.contrib import admin
from .models import Page, Theme, Site, Template
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'template', 'created')
    fields = ('title', 'site', 'description', 'content', 'template')
    save_as = True
    show_fall_result_count = True
    view_on_site = True

    def get_queryset(self, request):
        qs = super(PageAdmin, self).get_queryset(request)
        site = Site.objects.filter(author=request.user)
        return qs.filter(site=site)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "site":
            site = Site.objects.filter(author=request.user)
            kwargs['queryset'] = site
        return super(PageAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'created')


class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'theme', 'created')
    fields = ('name', 'theme')

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(SiteAdmin, self).get_queryset(request)
        return qs.filter(author=request.user)



admin.site.register(Page, PageAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Template, TemplateAdmin)
