import short_url
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Url(models.Model):
    url = models.URLField(max_length=1000)
    short_code = models.CharField(max_length=10, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_count = models.IntegerField(default=0)

    def __str__(self):
        return f"<URL {self.pk} >>{self.short_code}>"

@receiver(post_save, sender=Url)
def generate_short_code(sender, instance, created, **kwargs):
    if created and not instance.short_code:
        instance.short_code = short_url.encode_url(instance.pk)
        instance.save(update_fields=["short_code"])
