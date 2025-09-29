from guitar import Guitar


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

    def search_guitar(self, builder: str, model: str, guitar_type: str, backwood: str, topwood: str) -> Guitar | None:
        for guitar in self._guitars:
            if (guitar.builder.lower() == builder.lower() and
                guitar.model.lower() == model.lower() and
                guitar.guitar_type.lower() == guitar_type.lower() and
                guitar.backwood.lower() == backwood.lower() and
                guitar.topwood.lower() == topwood.lower()):
                return guitar
        return None

    