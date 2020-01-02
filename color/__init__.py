class Font:
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34


class Mode:
    DEFAULT = 0
    HIGH_LIGHT = 1
    UNDER_LINE = 4


class BackGround:
    BLACK = 40
    WHITE = 48


class Printer:
    def __init__(self, font: int, mode=Mode.DEFAULT, back_ground=BackGround.WHITE):
        self._mode = mode
        self._font = font
        self._back_ground = back_ground

    def __call__(self, text, end='\n'):
        print("\033[{};{};{}m{}\033[0m".format(self._mode, self._font, self._back_ground, text), end=end)


from functools import wraps


def _color_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        font_value = getattr(Font, func.__name__.upper())
        # print(font_value)
        if font_value is None:
            print("{},not supports yet".format(func.__name__))
        Printer(font=font_value)(*args, **kwargs)

    return wrapper


# how to use it?
@_color_decorator
def red(text, end='\n'):
    pass


@_color_decorator
def yellow(text, end='\n'):
    pass


@_color_decorator
def green(text, end='\n'):
    pass


@_color_decorator
def blue(text, end='\n'):
    pass


def color_it(text, end='\n'):
    colors = [30, 31, 32, 33, 34]
    import random
    for one_word in list(text):
        Printer(font=random.choice(colors))(one_word, end='')
    print("", end=end)


if __name__ == "__main__":
    red("红色！")