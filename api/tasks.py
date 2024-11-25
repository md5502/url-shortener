import logging

from celery import shared_task
from django.core.cache import cache

from .models import Url
from .utils import get_all_cache_keys

logger = logging.getLogger(__name__)



@shared_task
def sync_cache_to_db():
    """Synchronize URL data from Redis to the database."""
    try:
        cache_keys = get_all_cache_keys()
        if not cache_keys:
            logger.info("No cache keys found to sync.")
            return

        for key in cache_keys:
            logger.info(f"Processing cache key: {key}")  # noqa: G004

            short_code = key.split("-")[0]
            url_obj = Url.objects.filter(short_code=short_code).first()
            if not url_obj:
                logger.warning(f"No URL object found in DB for short_code: {short_code}")  # noqa: G004
                continue  # Move to the next key instead of stopping the loop

            access_count = cache.get(key)
            if access_count is not None:
                url_obj.access_count = access_count
                url_obj.save()
                cache.delete(key)

                logger.info(f"Updated URL object with short_code '{short_code}': {url_obj.access_count}")  # noqa: G004
            else:
                logger.warning(f"Cache key '{key}' has no value. Skipping update.")  # noqa: G004

    except Exception as e:
        logger.error(f"Error in sync_cache_to_db task: {e}", exc_info=True)  # noqa: G004, G201
        raise
