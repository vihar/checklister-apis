from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


class TimeAuditModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Created At",)
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Last Modified At")

    class Meta:
        abstract = True


class Item(TimeAuditModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    description_html = models.TextField(editable=False, blank=True)
    details = JSONField(null=True)
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='items',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.name
