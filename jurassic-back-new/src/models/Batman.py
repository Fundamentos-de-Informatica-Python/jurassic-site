class Batman:

    """
    type: carnivoro | hervivoro | etc
    """

    def __init__(self, type, name, weight, age) -> None:
        self.type   = type
        self.name   = name
        self.weight = weight
        self.height = age

    def serialize(self):
        return {
            'type': self.type,
            'name': self.name,
            'weight': self.weight,
            'height': self.height,
            'long': self.age
        }


