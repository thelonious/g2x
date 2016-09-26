import sys

ESC       = chr(27)
CLEAR     = ESC + "[2J"
MOVE_HOME = ESC + "[H"
ERASE     = CLEAR + MOVE_HOME

LINES = 24
COLS = 80


class Display:
    def __init__(self, title):
        self.title = title

    def clear(self):
        sys.stdout.write(ERASE)

    def show_properties(self, properties, names=None):
        self.clear()
        self.print(self.title)
        print()

        if names is None:
            for k, v in properties.items():
                self.print("{0}: {1}".format(k, v))
        else:
            for k in names:
                self.print("{0}: {1}".format(k, properties[k]))

    def print(self, message):
        print(message, end="\x0a\x0d")
