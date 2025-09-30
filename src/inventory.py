from guitar import Guitar
from builder import Builder
from guitar_type import GuitarType
from guitar_string_number import GuitarStringNumber
from wood import Wood


class Inventory:
    def __init__(self):
        self._guitars: list[Guitar] = []

    def add_guitar(self, guitar: Guitar) -> None:
        self._guitars.append(guitar)

    def remove_guitar(self, guitar: Guitar) -> None:
        if guitar in self._guitars:
            self._guitars.remove(guitar)

    def get_guitars(self) -> list[Guitar]:
        return self._guitars

    def search_guitar(self, builder: Builder, model: str, guitar_type: GuitarType, backwood: Wood, topwood: Wood, strings: GuitarStringNumber) -> list[Guitar] | None:
        guitars: list[Guitar] = []

        for guitar in self._guitars:
            if (guitar.get_guitar_spec().builder == builder and
                guitar.get_guitar_spec().model.lower() == model.lower() and
                guitar.get_guitar_spec().guitar_type == guitar_type and
                guitar.get_guitar_spec().backwood == backwood and
                guitar.get_guitar_spec().topwood == topwood and
                guitar.get_guitar_spec().strings == strings):
                guitars.append(guitar)

        return guitars if guitars else None
    