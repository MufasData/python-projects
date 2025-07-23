# Elementary practice with classes

class Bird:
    def __init__(self,species,color):
        self.color = color
        self.species = species

my_bird = Bird('toucan','black')

print(f"My bird is a {my_bird.species} and it has the color {my_bird.color}.")

    