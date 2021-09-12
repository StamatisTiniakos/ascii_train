# -*- coding: UTF-8 -*-

"""
ascii_train.train
~~~~~~~~~~
Core components for train.
"""

_TRAIN_MAPING = {'HF': '<HHHH', 'HB': 'HHHH>',
                 'P': '|OOOO|', 'R': '|hThT|', 'C': '|____|', 'F': '|^^^^|'}


class IllegalStateException(Exception):
    """Filling a train that is already full should throw exception"""


class Train(object):
    def __init__(self, string_train):
        '''
        Class implementing Train Object
        '''
        self.string_train = string_train
        self.ascii_train = self._get_ascii_train()

    def _get_ascii_train(self):
        train_list = []
        train_length = len(self.string_train)
        for i, char in enumerate(self.string_train):
            if i == 0 and char == 'H':
                train_list.append(_TRAIN_MAPING['HF'])
            elif i == train_length-1 and char == 'H':
                train_list.append(_TRAIN_MAPING['HB'])
            else:
                train_list.append(_TRAIN_MAPING[char])

        return train_list

    def print(self):
        return "::".join(self.ascii_train)

    def detach_head(self):
        if len(self.string_train) > 0:
            self.string_train = self.string_train[1:]
            self.ascii_train.pop(0)
        else:
            print("No train wagon left, add one and try again!")

    def detach_end(self):
        if len(self.string_train) > 0:
            self.string_train = self.string_train[:-1]
            self.ascii_train.pop()
        else:
            print("No train wagon left, add one and try again!")

    def fill(self):
        if 'C' not in self.string_train:
            raise IllegalStateException
        string_list = list(self.string_train)
        for i, char in enumerate(string_list):
            if char == "C":
                string_list[i] = 'F'
                break
        self.string_train = ''.join(string_list)
        self.ascii_train = self._get_ascii_train()
