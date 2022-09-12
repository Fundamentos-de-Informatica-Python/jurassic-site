class Dinos:

    """
    type: carnivoro | hervivoro | etc
    name: trex | raptor | argentinosaurio | mosassaurio | etc
    """

    def __init__(self, type, name, weight, height, long, img) -> None:
        self.type   = type
        self.name   = name
        self.weight = weight
        self.height = height
        self.long   = long
        self.img    = img

    def serialize(self):
        return {
            'type': self.type,
            'name': self.name,
            'weight': self.weight,
            'height': self.height,
            'long': self.long,
            'img': self.img
        }


