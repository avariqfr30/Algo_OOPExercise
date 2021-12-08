class Fancy_List:
    def __init__(self, type, weight):
        self.type = type
        self.weight = weight
        self.price = 0
        self.calc_price = 0

    def get_price(self):
        return self.price

    def set_price(self, amnt):
        self.price = amnt

    def price_list(self):
        if self.type == "Dry Cured Iberian Ham":
            self.set_price(177.8)

        elif self.type == "Wagyu Steaks":
            self.set_price(450)

        elif self.type == "Matsutake Mushrooms":
            self.set_price(272)

        elif self.type == "Kopi Luwak Coffee":
            self.set_price(306.5)

        elif self.type == "Moose Cheese":
            self.set_price(487.2)

        elif self.type == "White Truffles":
            self.set_price(3600)

        elif self.type == "Blue Fin Tuna":
            self.set_price(3603)

        elif self.type == "Le Bonnotte Potatoes":
            self.set_price(270.81)

    def food_cost(self):
        self.price_list()
        self.calc_price = self.price * self.weight
        return self.calc_price