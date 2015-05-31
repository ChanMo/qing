from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from page.models import Page, Site, Theme

# Create your views here.
class IndexView(TemplateView):
    template_name = "page/home.html"


class SiteView(TemplateView):
    modal = Site

    def get_site(self):
        site = Site.objects.get(id=self.kwargs['site_id'])
        return site

    def get_context_data(self, **kwargs):
        context = super(SiteView, self).get_context_data(**kwargs)
        site = self.get_site()
        context['page_list'] = Page.objects.filter(site=site,parent=None)
        return context

    def get_template_names(self):
        site = self.get_site()
        self.theme = Theme.objects.get(id=site.theme_id)
        return ("page/"+self.theme.value+"/index.html", "page/default/index.html")


class PageView(DetailView):
    model = Page
    context_object_name = "page"

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        context['child_page'] = Page.objects.filter(parent=self.object.id)
        return context

    def get_template_names(self):
        site = Site.objects.get(id=self.object.site_id)
        theme = Theme.objects.get(id=site.theme_id)
        return ("page/"+theme.value+"/"+self.object.template.value+".html", "page/default/detail.html")
