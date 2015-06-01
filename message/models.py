from django.db import models
from page.models import Site
# Create your models here.

class Message(models.Model):
    site = models.ForeignKey(Site, related_name='Message', default='1')
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=11)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
