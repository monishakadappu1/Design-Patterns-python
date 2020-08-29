class Frog:
    def __init__(self,name):
        self._name = name

    def __str__(self):
        return self._name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = "{} encounters an obstacle {} and {}".format(self, obstacle, act)
        print(msg)


class Bug:
    def __str__(self):
        return "a bug"

    def action(self):
        return "eats it"


class FrogWorld:
    def __init__(self, name):
        print(self)
        self.playername = name

    def __str__(self):
        return "\n\n\t------FrogWorld--------"

    def make_character(self):
        frog = Frog(self.playername)
        return frog

    def make_obstacle(self):
        return Bug()


class Wizard:
    def __init__(self,name):
        self._name = name

    def __str__(self):
        return self._name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = "{} encounters an obstacle {} and {}".format(self, obstacle, act)
        print(msg)


class Ork:
    def __str__(self):
        return "an Ork"

    def action(self):
        return "kills it"


class WizardWorld:
    def __init__(self,name):
        print(self)
        self.playername = name

    def __str__(self):
        return "\n\n\t----------Wizard World--------"

    def make_character(self):
        return Wizard(self.playername)

    def make_obstacle(self):
        return Ork()


# abstract class in action
class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_game(name):
    try:
        age = input("Welcome {}, What is your age".format(name))
        age = int(age)
    except ValueError as V:
        print("{} is invalid please try again".format(age))
        return False, age
    return True,age


def main():
    name = input("Hello , What is your name?")
    valid_user = False
    while not valid_user:
        valid_user, age = validate_game(name)
    game = FrogWorld(name) if age<18 else WizardWorld(name)
    environment = GameEnvironment(game)
    environment.play()


if __name__ == "__main__":
    main()
    #wz = WizardWorld("")


