import requests

import configuration


def post_new_order(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body,
        timeout=15,
    )


def get_order_by_track(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.ORDER_BY_TRACK_PATH,
        params={"t": track},
        timeout=15,
    )