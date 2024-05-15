#!/usr/bin/env python3
""" web """

import requests
import redis
from functools import wraps
from typing import Callable

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Tracks how many times a particular URL was accessed
    in the key "count:{url}" and cache the result with an expiration
    time of 10 seconds.
    """
    @wraps(method)
    def wrapper(url):
        r.incr(f"count:{url}")
        cached_html = r.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Obtains the HTML content of a particular URL and returns it."""
    req = requests.get(url)
    return req.text


if __name__ == "__main__":
    html_content = get_page('http://slowwly.robertomurray.co.uk')
    print(html_content)
