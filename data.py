from datetime import date, timedelta

order_body = {
    "firstName": "Ольга",
    "lastName": "Иванова",
    "address": "Тестовая, 101",
    "metroStation": 45,
    "phone": "+79990000000",
    "rentTime": 2,
    "deliveryDate": (date.today() + timedelta(days=1)).isoformat(),
    "comment": "Автотест",
    "color": ["BLACK"],
}