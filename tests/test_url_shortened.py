import pytest
from game.app.url_shortened import URLShortened, URLShortenedKeyError, URLShortenedCapacityError, \
    URLShortenedEmptyAvailableUrlsError

base_url = "https://www.revolut.com/rewards-personalised-cashback-and-discounts/"


def test_original_equal_short():
    us = URLShortened()
    short = us.encode_by_counter(base_url)
    assert base_url == us.decode_url(short)


def test_single_encode():
    us = URLShortened()
    short = us.encode_by_counter(base_url)
    assert short == 'https://www.rev.me/1'


def test_multi_decode():
    us = URLShortened()
    short = us.encode_by_counter(base_url)
    assert short == 'https://www.rev.me/1'
    short = us.encode_by_counter(base_url)
    assert short == 'https://www.rev.me/2'


def test_ex():
    us = URLShortened()
    with pytest.raises(URLShortenedKeyError):
        us.decode_url("abc")


def test_cap():
    us = URLShortened("https://www.rev.me/", capacity=2)
    us.encode_by_counter("a")
    us.encode_by_counter("b")
    with pytest.raises(URLShortenedCapacityError):
        us.encode_by_counter("c")


def test_predefined_identifiers():
    predefined_pool = [str(i) for i in range(1, 10)]
    us = URLShortened("https://www.rev.me/", 2, predefined_pool)
    short_url = us.encode_by_available_list("a")
    assert 1 <= int(short_url.split('/')[-1]) <= 100
    assert short_url == 'https://www.rev.me/1'
    assert us.decode_url(short_url) == "a"


def test_predefined_identifiers_capacity():
    predefined_pool = [str(i) for i in range(1, 101)]
    us = URLShortened("https://www.rev.me/", 2, predefined_pool)
    short_url = us.encode_by_available_list("a")
    assert 1 <= int(short_url.split('/')[-1]) <= 100
    short_url = us.encode_by_available_list("b")
    assert 1 <= int(short_url.split('/')[-1]) <= 100
    with pytest.raises(URLShortenedCapacityError):
        us.encode_by_available_list("c")


def test_predefined_identifiers_pool_limit():
    predefined_pool = [str(i) for i in range(1, 2)]
    us = URLShortened("https://www.rev.me/", 100, predefined_pool)
    short_url = us.encode_by_available_list("a")
    assert 1 <= int(short_url.split('/')[-1]) <= 100
    with pytest.raises(URLShortenedEmptyAvailableUrlsError):
        us.encode_by_available_list("c")


def test_predefined_identifiers_multi_urls():
    origin_urls = ['a', 'b', 'c']
    predefined_pool = [str(i) for i in range(1, 4)]
    us = URLShortened("https://www.rev.me/", 100, predefined_pool)
    shorter_urls = []
    for url in origin_urls:
        shorter_urls.append(us.encode_by_available_list(url))
    vis = set()
    cnt = 0
    for short_url in shorter_urls:
        origin_url = us.decode_url(short_url)
        assert origin_url in origin_urls
        if origin_url not in vis:
            vis.add(origin_url)
            cnt += 1
    assert cnt == len(origin_urls)
