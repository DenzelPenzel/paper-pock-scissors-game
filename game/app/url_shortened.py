"""
https://www.revolut.com/rewards-personalised-cashback-and-discounts/

Expected output:
https://www.rev.me/<url identifier>

<url identifier> - (dynamic length, based on config)

https://www.rev.me/1 -> https://www.revolut.com/rewards-personalised-cashback-and-discounts/
https://www.rev.me/2 -> https://www.revolut.com/rewards-personalised-cashback-and-discounts/

https://www.rev.me/...

https://www.revolut.com/rewards-personalised-cashback-and-discounts/: -> [https://www.rev.me/1, https://www.rev.me/2]


from uuid import uuid4
self.predefined_identifiers = [str(uuid4()) for _ in range(capacity)]

"""
import random
from typing import List


class URLShortened:
    def __init__(self, base_url: str = "https://www.rev.me/", capacity: int = 100,
                 predefined_identifiers=None):
        if predefined_identifiers is None:
            predefined_identifiers = []
        self.base_url = base_url.rstrip("/") + '/'
        self.counter = 1
        self.short_to_original = {}
        self.max_urls = capacity
        self.available_list = set(predefined_identifiers)

    def encode_by_available_list(self, original_url: str) -> str:
        if len(self.short_to_original) >= self.max_urls:
            raise URLShortenedCapacityError("Reached max num of URLs")

        if not self.available_list:
            raise URLShortenedEmptyAvailableUrlsError("No available urls")

        short_id = random.choice(list(self.available_list))
        self.available_list.remove(short_id)
        short_url = self.base_url + short_id
        self.short_to_original[short_url] = original_url
        return short_url

    def encode_by_counter(self, original_url: str) -> str:
        if len(self.short_to_original) >= self.max_urls:
            raise URLShortenedCapacityError("Max num of URLs")
        short_url = self.base_url + str(self.counter)
        self.counter += 1
        self.short_to_original[short_url] = original_url
        return short_url

    def decode_url(self, short_url):
        if short_url in self.short_to_original:
            return self.short_to_original[short_url]
        else:
            raise URLShortenedKeyError("Short URL doesnt exists")


class URLShortenedCapacityError(Exception):
    """Base class for URLShortened custom exception"""


class URLShortenedKeyError(Exception):
    """Base class for URLShortened custom exception"""


class URLShortenedEmptyAvailableUrlsError(Exception):
    """Base class for URLShortened custom exception"""
