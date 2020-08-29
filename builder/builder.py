from enum import Enum
import time

PizzaProgress = Enum("PizzaProgress", "queued preparation baking ready")
PizzaDough = Enum("PizzaDough", "thin thick")
PizzaSauce = Enum("PizzaSauce","tomato creme_fraiche")
PizzaTopping = Enum("PizzaTopping", "mozzarella double_mozzarella bacon ham mushrooms red_onion oregano")

STEP_DELAY = 3


class Pizza:

    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print("preparing the {} dough for your {}...".format(self.dough,self))
        time.sleep(STEP_DELAY)
        print(f"done with {self.dough} dough")


class MargaritaBuilder:

    def __init__(self):
        self.pizza = Pizza("margarita")
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough("thin")

    def add_sauce(self):
        print("adding tomato sauce to your Margarita")
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print("done with the tomato sauce")

    def add_topping(self):
        topping_desc = "double_mozzarella, oregano"
        topping_items = (PizzaTopping.double_mozzarella, PizzaTopping.oregano)
        print("adding the toppings {} to your margarita".format(topping_desc))
        self.pizza.topping.append([topping for topping in topping_items])
        time.sleep(STEP_DELAY)
        print("done with toppings {}".format(topping_desc))

    def bake(self):
        self.progress = PizzaProgress.baking
        print("baking your Margarita for {} seconds".format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print("Your margarita is ready")


class CreamyBaconBuilder:

    def __init__(self):
        self.pizza = Pizza("creamy bacon")
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    # just a wrapper to inner dough
    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough("thick")

    def add_sauce(self):
        print("adding creme fraiche sauce to your creamy bacon")
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print("done with the creme fraiche sauce")

    def add_topping(self):
        topping_desc = "mozzarella, bacon, ham, mushrooms, red_onion, oregano"
        topping_items = (PizzaTopping.mozzarella,
                         PizzaTopping.bacon,
                         PizzaTopping.ham,
                         PizzaTopping.mushrooms,
                         PizzaTopping.red_onion,
                         PizzaTopping.oregano)
        print("adding the toppings {} to your creamy Bacon".format(topping_desc))
        self.pizza.topping.append([topping for topping in topping_items])
        time.sleep(STEP_DELAY)
        print("done with toppings {}".format(topping_desc))

    def bake(self):
        self.progress = PizzaProgress.baking
        print("baking your Creamy Bacon for {} seconds".format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print("Your Creamy Bacon is ready")


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        steps = (builder.prepare_dough,
                 builder.add_sauce,
                 builder.add_topping,
                 builder.bake)
        [step() for step in steps]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        msg = "What pizza would you like, [m]argarita or [c]reamy bacon?"
        pizza_style = input(msg)
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError:
        error_msg = "Sorry, only margarita (key m) or creamy bacon (key c) available"
        print(error_msg)
        valid_input = False
        return valid_input, None
    return valid_input, builder

def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
    valid_input = False
    builder = None
    while not valid_input:
        valid_input, builder = validate_style(builders)
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print(f"Enjoy your {pizza} pizza")

if __name__ == "__main__":
    main()









