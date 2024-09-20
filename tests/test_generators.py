import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency1(fo_filter_and_transaction1) -> None:
    assert next(filter_by_currency(fo_filter_and_transaction1)) == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]


def test_filter_by_currency2(fo_filter_and_transaction2) -> None:
    assert next(filter_by_currency(fo_filter_and_transaction2)) == [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


def test_filter_by_currency_missing() -> None:
    assert next(
        filter_by_currency(
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "", "code": ""}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ]
        )
    ) == [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "", "code": ""}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


def test_filter_by_currency_missing1() -> None:
    with pytest.raises(AssertionError):
        assert next(
            filter_by_currency(
                [
                    {
                        "id": 142264268,
                        "state": "EXECUTED",
                        "date": "2019-04-04T23:20:05.206878",
                        "operationAmount": {"amount": "79114.93", "currency": {"name": "", "code": ""}},
                        "description": "Перевод со счета на счет",
                        "from": "Счет 19708645243227258542",
                        "to": "Счет 75651667383060284188",
                    },
                ]
            )
        ) == [
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "", "code": ""}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            },
        ]


def test_filter_by_currency_empty() -> None:
    assert next(filter_by_currency([])) == ([])


def test_transaction_descriptions(fo_filter_and_transaction1) -> None:
    assert next(transaction_descriptions(fo_filter_and_transaction1)) == "Перевод организации"


def test_transaction_descriptions2(fo_filter_and_transaction2) -> None:
    assert next(transaction_descriptions(fo_filter_and_transaction2)) == "Перевод со счета на счет"


def test_transaction_descriptions_empty() -> None:
    assert next(transaction_descriptions([])) == ([])


def test_transaction_descriptions_empty1() -> None:
    with pytest.raises(StopIteration):
        assert next(transaction_descriptions([])) == ([])


@pytest.mark.parametrize("start, stop, expected",
    [(1, 1, "0000 0000 0000 0001"), (9999999999999999, 9999999999999999, "9999 9999 9999 9999"),
     (1000, 1001, "0000 0000 0000 1000")],
)
def test_card_number_generator(start: int, stop: int, expected: str) -> None:
    assert next(card_number_generator(start, stop)) == expected

def test_card_number_generator_range(start: int = 1, stop: int = 5) -> None:
    generated_number = card_number_generator(1, 5)
    assert next(generated_number) == "0000 0000 0000 0001"
    assert next(generated_number) == "0000 0000 0000 0002"
    assert next(generated_number) == "0000 0000 0000 0003"
    assert next(generated_number) == "0000 0000 0000 0004"
    assert next(generated_number) == "0000 0000 0000 0005"