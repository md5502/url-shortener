from django.core.cache import cache, caches

CACHE_TIMEOUT = 20  # Cache expiry timeout in seconds


def get_cached_url(short_code):
    url_key = short_code + "-url"
    counter_key = short_code + "-counter"
    url = cache.get(url_key)
    if url:
        counter = cache.get(counter_key)
        counter += 1
        cache.set(counter_key, counter)
        return url
    return None


def set_cached_url(short_code, url, access_count=0):
    """this function save data to the cache whit tow deferent keys
    one for the url and the other for the counter
    """
    cache.set(f"{short_code}-url", url, CACHE_TIMEOUT)
    cache.set(f"{short_code}-counter", access_count)


def update_cache(short_code, url):
    cache.set(f"{short_code}-url", url, CACHE_TIMEOUT)

def delete_cache(short_code):
    cache.delete(f"{short_code}-url")
    cache.delete(f"{short_code}-counter")



def get_all_cache_keys() -> list[str]:
    """Fetch all Redis cache keys ending with '-counter'."""
    try:
        redis_cache = caches["default"]  # Avoid overriding the global `cache`
        redis_client = redis_cache.client.get_client()

        keys = redis_client.keys("*")
        return [
            key.decode("utf-8").split(":")[-1]
            for key in keys if key.decode("utf-8").split(":")[-1].endswith("-counter")
        ]
    except Exception as e:
        print(f"Error fetching cache keys: {e}")  # noqa: T201
        return []

