import pandas as pd
from pandas import DataFrame

from src.reports import spending_by_category


def test_spending_by_category() -> None:
    """тест для функции которая возвращает траты по заданной категории за последние три месяца (от переданной даты)."""
    data = DataFrame(
        [
            {
                "Дата операции": "01.01.2018 20:27:51",
                "Дата платежа": "04.01.2018",
                "Номер карты": "*7197",
                "Статус": "OK",
                "Сумма операции": -316.0,
                "Валюта операции": "RUB",
                "Сумма платежа": -316.0,
                "Валюта платежа": "RUB",
                "Кэшбэк": "",
                "Категория": "Красота",
                "MCC": 5977.0,
                "Описание": "OOO Balid",
                "Бонусы (включая кэшбэк)": 6,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 316.0,
            },
            {
                "Дата операции": "01.01.2018 12:49:53",
                "Дата платежа": "01.01.2018",
                "Номер карты": "",
                "Статус": "OK",
                "Сумма операции": -3000.0,
                "Валюта операции": "RUB",
                "Сумма платежа": -3000.0,
                "Валюта платежа": "RUB",
                "Кэшбэк": "",
                "Категория": "Переводы",
                "MCC": "",
                "Описание": "Линзомат ТЦ Юность",
                "Бонусы (включая кэшбэк)": 0,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 3000.0,
            },
        ]
    )

    expected_result = DataFrame(
        [
            {
                "Дата операции": "01.01.2018 12:49:53",
                "Дата платежа": "01.01.2018",
                "Номер карты": "",
                "Статус": "OK",
                "Сумма операции": -3000.0,
                "Валюта операции": "RUB",
                "Сумма платежа": -3000.0,
                "Валюта платежа": "RUB",
                "Кэшбэк": "",
                "Категория": "Переводы",
                "MCC": "",
                "Описание": "Линзомат ТЦ Юность",
                "Бонусы (включая кэшбэк)": 0,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 3000.0,
            }
        ]
    )

    result = spending_by_category(data, "Переводы", "01.01.2018 20:27:51")

    pd.testing.assert_frame_equal(
        result.reset_index(drop=True), expected_result.reset_index(drop=True)
    )
