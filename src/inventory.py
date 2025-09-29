from guitar import Guitar
from builder import Builder
from guitar_type import GuitarType
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

    def search_guitar(self, builder: Builder, model: str, guitar_type: GuitarType, backwood: Wood, topwood: Wood) -> Guitar | None:
        for guitar in self._guitars:
            if (guitar.builder == builder and
                guitar.model.lower() == model.lower() and
                guitar.guitar_type == guitar_type and
                guitar.backwood == backwood and
                guitar.topwood == topwood):
                return guitar
        return None

    