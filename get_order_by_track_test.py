# Даниил Меньшиков, 50-я когорта — финальный проект «Яндекс Самокат»

import configuration
import data
import sender_stand_request


def test_get_order_by_track():
    assert configuration.URL_SERVICE, "Укажи адрес стенда в configuration.py"

    created = sender_stand_request.post_new_order(data.order_body)
    assert created.status_code == 201, f"Создание заказа: HTTP {created.status_code}"

    track = created.json().get("track")
    assert track is not None, "В ответе на создание заказа нет трек-номера"

    response = sender_stand_request.get_order_by_track(track)
    assert response.status_code == 200, f"Получение заказа: HTTP {response.status_code}"