import re
from random import randint


def generator(text, sep=" ", option=None):
    if type(text) is not str:
        print('ERROR')
        return
    if type(sep) is not str or not sep:
        print('ERROR')
        return
    split_text = text.split(sep)
    if option == 'shuffle':
        idx_orders = []
        while len(idx_orders) != len(split_text):
            new_idx = randint(0, len(split_text) - 1)
            if new_idx not in idx_orders:
                idx_orders.append(new_idx)
        new_split = [split_text[idx] for idx in idx_orders]
        split_text = new_split
    elif option == 'unique':
        new_split = []
        for word in split_text:
            if word not in new_split:
                new_split.append(word)
        split_text = new_split
    elif option == 'ordered':
        convert = lambda text: int(text) if text.isdigit() else text
        alphanum_key = lambda key: [convert for c in re.split('([0-9]+)', key)]
        split_text.sort(key=alphanum_key)
    for word in split_text:
        yield word
