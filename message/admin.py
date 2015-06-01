from django.contrib import admin
from page.models import Site
from .models import Message
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ('site', 'name', 'mobile', 'content', 'created')
    fields = ('site', 'name', 'mobile', 'content', 'created')
    readonly_fields = Message._meta.get_all_field_names()

    def get_queryset(self, request):
        qs = super(MessageAdmin, self).get_queryset(request)
        site = Site.objects.filter(author=request.user)
        return qs.order_by('-created').filter(site=site)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Message, MessageAdmin)
