import redis

def get_cache():
    return redis.Redis(host='localhost', port=6379, db=0)

def cached_resolve(domain, resolve_func):
    cache = get_cache()
    if cache.exists(domain):
        return cache.get(domain).decode()
    else:
        result = resolve_func(domain)
        cache.set(domain, result, ex=3600)  # Cache for 1 hour
        return result
