import random

""" Implementation is suited for Oxylabs Residential Proxies (https://oxylabs.io/products/residential-proxy-pool).
If you decide to use different service for proxies you'll need to make some minor code adjustments. """


def get_proxies():
    username = "your_username"
    password = "your_password"
    country = "us"
    s_id = random.randrange(1, 10000)

    entry = "http://customer-%s-cc-%s-sessid-%s:%s@pr.oxylabs.io:7777" % (
        username,
        country,
        s_id,
        password,
    )

    proxies = {"http:": entry, "https": entry}

    return proxies
