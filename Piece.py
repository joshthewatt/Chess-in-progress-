def LetterToNumber(location):
    letter = location[0]
    if letter == "A":
        return ("1" + location[1])
    if letter == "B":
        return ("2" + location[1])
    if letter == "C":
        return ("3" + location[1])
    if letter == "D":
        return ("4" + location[1])
    if letter == "E":
        return ("5" + location[1])
    if letter == "F":
        return ("6" + location[1])
    if letter == "G":
        return ("7" + location[1])
    if letter == "H":
        return ("8" + location[1])

    
class Piece(object):

    def __init__(self, name, location):
        self.location = location #[Number][Number]
        self.name = name #[Piece Type][number]
    def move(self, newlocation):
        self.location = newlocation
    #def delete(self):


class whitePawn(Piece):
    def __init__(self, name, location):
        Piece.__init__(self, name, location)
    def move(self, newlocation):
        if newlocation != (self.location % 10) + 1:
            print("Cannot move there")


