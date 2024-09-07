from src.widget import mask_account_card, get_date

def test_masks():
    assert mask_account_card("Счет 64686473678894779589") == 'Счет **9589'
    assert mask_account_card("MasterCard 7158300734726758") == 'MasterCard 7158 30** **** 6758'
    assert mask_account_card("Visa Gold 5999414228426353") == 'Visa Gold 5999 41** **** 6353'

    assert get_date("2024-03-11T02:26:18.671407") == '11.03.2024'
