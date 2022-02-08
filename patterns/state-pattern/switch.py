

class Switch(object):
    def __init__(self):
        self.__class__ = OffState


class OffState(object):
    def on(self):
        print('turning on')
        self.__class__ = OnState


class OnState(object):
    def off(self):
        print('turning off')
        self.__class__ = OffState


def main():
    switch = Switch()
    switch.on()
    switch.off()


if __name__ == '__main__':
    main()
