import sys


def trim_doc(docstring):
    if not docstring:
        return ''
    lines = docstring.expandtabs().splitlines()
    indent = sys.maxsize
    for line in lines[1:]:
        stripped = line.rstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    trimmed = [lines[0].strip()]
    if indent < sys.maxsize:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    return '\n'.join(trimmed)


class GotCharacter:
    def __init__(self, first_name=None, is_alive=True):
        self.__doc__ = trim_doc('Generic class for any GOT character')
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super(Stark, self).__init__(first_name=first_name, is_alive=is_alive)
        self.__doc__ = trim_doc('A class representing the Stark family. Or when bad things'
                                'happen to good people.')
        self.family_name = 'Stark'
        self.house_words = 'Winter is coming'

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


class Lannister(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super(Lannister, self).__init__(first_name=first_name, is_alive=is_alive)
        self.__doc__ = trim_doc('A class representing the Lannister family.')
        self.family_name = 'Lannister'
        self.house_words = 'A Lannister always pays his debts'

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
