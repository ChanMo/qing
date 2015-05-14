from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from page.models import Page, Site

# Create your views here.
class SiteView(TemplateView):
    template_name = "page/index.html"
    def get_context_data(self, **kwargs):
        context = super(SiteView, self).get_context_data(**kwargs)
        site = Site.objects.filter(author=context['site_id'])
        context['page_list'] = Page.objects.filter(site=site,parent=None)
        return context


class IndexView(ListView):
    model = Page
    template_name = "page/index.html"
    context_object_name = "page_list"


class PageView(DetailView):
    model = Page
    # template_name = "page/detail.html"
    context_object_name = "page"

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        context['child_page'] = Page.objects.filter(parent=context['title'])
        return context

    def get_template_names(self):
        return ("page/"+self.object.template.value+".html", "page/detail.html")
