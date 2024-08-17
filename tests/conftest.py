import pytest


@pytest.fixture
def transactions():
    return [
        {
            "operation_date": "27.09.2019 13:05:37",
            "payment_date": "29.09.2019",
            "card_number": "*7197",
            "status": "OK",
            "operation_sum": -144.45,
            "operation_cur": "RUB",
            "payment_sum": -144.45,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Супермаркеты",
            "MCC": 5499.0,
            "description": "Колхоз",
            "Bonus": 2,
            "Invest_bank": 0,
            "rounded_operation_sum": 144.45,
        },
        {
            "operation_date": "27.09.2019 04:17:51",
            "payment_date": "27.09.2019",
            "card_number": "*4556",
            "status": "OK",
            "operation_sum": 1000.0,
            "operation_cur": "RUB",
            "payment_sum": 1000.0,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Бонусы",
            "MCC": 0,
            "description": 'Пополнение. Тинькофф Банк. Бонус по акции "Приведи друга"',
            "Bonus": 0,
            "Invest_bank": 0,
            "rounded_operation_sum": 1000.0,
        },
        {
            "operation_date": "26.09.2019 18:12:45",
            "payment_date": "26.09.2019",
            "card_number": "*4556",
            "status": "OK",
            "operation_sum": 250.0,
            "operation_cur": "RUB",
            "payment_sum": 250.0,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Пополнения",
            "MCC": 0,
            "description": "Пополнение через Альфа-Банк",
            "Bonus": 0,
            "Invest_bank": 0,
            "rounded_operation_sum": 250.0,
        },
        {
            "operation_date": "26.09.2019 17:42:59",
            "payment_date": "28.09.2019",
            "card_number": "*7197",
            "status": "OK",
            "operation_sum": -177.1,
            "operation_cur": "RUB",
            "payment_sum": -177.1,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Супермаркеты",
            "MCC": 5411.0,
            "description": "SPAR",
            "Bonus": 3,
            "Invest_bank": 0,
            "rounded_operation_sum": 177.1,
        },
        {
            "operation_date": "26.09.2019 11:57:20",
            "payment_date": "27.09.2019",
            "card_number": "*7197",
            "status": "OK",
            "operation_sum": -357.22,
            "operation_cur": "RUB",
            "payment_sum": -357.22,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Отели",
            "MCC": 7011.0,
            "description": "Dongying Luxury Blue Hori",
            "Bonus": 7,
            "Invest_bank": 0,
            "rounded_operation_sum": 357.22,
        },
    ]


@pytest.fixture
def operations_1():
    return [
        {
            "Дата операции": "29.12.2021 16:22:08",
            "Дата платежа": "29.12.2021",
            "Номер карты": "*5091",
            "Статус": "OK",
            "Сумма операции": -120.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -120.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": 0,
            "Категория": "Фастфуд",
            "MCC": 5814,
            "Описание": "Mouse Tail",
            "Бонусы (включая кэшбэк)": 1,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 120.0,
        },
        {
            "Дата операции": "26.12.2021 22:09:56",
            "Дата платежа": "27.12.2021",
            "Номер карты": "*5091",
            "Статус": "OK",
            "Сумма операции": -415.32,
            "Валюта операции": "RUB",
            "Сумма платежа": -415.32,
            "Валюта платежа": "RUB",
            "Кэшбэк": 0,
            "Категория": "Фастфуд",
            "MCC": 7512,
            "Описание": "Ситидрайв",
            "Бонусы (включая кэшбэк)": 20,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 415.32,
        },
    ]
