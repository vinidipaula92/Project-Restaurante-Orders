class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.inventory = {**self.MINIMUM_INVENTORY}

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if self.inventory[ingredient] < 1:
                return False
            self.inventory[ingredient] -= 1

    def get_quantities_to_buy(self):
        return {k: max(0, self
                       .MINIMUM_INVENTORY[k] - self
                       .inventory[k]) for k in self.inventory}

    def get_available_dishes(self):
        return {k for k, v in self
                .INGREDIENTS.items() if all(self.inventory[i] > 0 for i in v)}
