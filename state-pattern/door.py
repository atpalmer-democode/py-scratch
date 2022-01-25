

def Door():
    return LockedDoor()


class LockedDoor(object):
    def key(self):
        print('Unlocking')
        self.__class__ = ClosedDoor

    def handle(self):
        print("Can't open locked door")


class ClosedDoor(object):
    def handle(self):
        print('Opening')
        self.__class__ = OpenDoor

    def key(self):
        print('Locking')
        self.__class__ = LockedDoor


class OpenDoor(object):
    def handle(self):
        print('Closing')
        self.__class__ = ClosedDoor

    def key(self):
        print("Can't lock open door")


def main():
    door = Door()
    assert type(door) is LockedDoor
    door.key()
    assert type(door) is ClosedDoor
    door.key()
    assert type(door) is LockedDoor
    door.key()
    door.handle()
    assert type(door) is OpenDoor
    door.key()  # Can't lock open door
    assert type(door) is OpenDoor
    door.handle()
    assert type(door) is ClosedDoor
    door.key()
    assert type(door) is LockedDoor
    door.handle()  # Can't open locked door


if __name__ == '__main__':
    main()
