def get_mask_card_number(card_number):
    return card_number[:4] + ' ' + card_number[5:7] + '*' * len(card_number[7:9]) + ' ' + '*' * len(card_number[8:13]) + ' '  + card_number[-4:]

print(get_mask_card_number('123456789876'))