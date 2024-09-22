import short_url
from django.db import models


class Url(models.Model):
    full_url = models.URLField(db_index=True)
    short_url = models.CharField(max_length=20, db_index=True, blank=True, unique=True)
    counter = models.IntegerField(default=0)  # Initialize counter to 0

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_url

    def save(self, *args, **kwargs):
        if not self.short_url:  # Only generate short_url if it doesn't exist
            super().save(*args, **kwargs)  # Save first to generate the ID
            self.short_url = short_url.encode_url(self.id)
        super().save(*args, **kwargs)
