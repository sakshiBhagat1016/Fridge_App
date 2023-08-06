from utils.validator import validate_input


class FridgeService:
    def __init__(self, fridge):
        self.fridge = fridge

    def insert_item(self, name, quantity):
        name = validate_input(name, "^[A-Za-z0-9_-]+$", "Invalid item name")
        quantity = validate_input(
            quantity, "^[0-9]+(\\.[0-9]+)? (Kg|Ltrs)$", "Invalid quantity")
        self.fridge.insert_item(name, quantity)

    def consume_item(self, name, consumption):
        name = validate_input(name, "^[A-Za-z0-9_-]+$", "Invalid item name")
        consumption = validate_input(
            consumption, "^[0-9]+(\\.[0-9]+)? (Kg|Ltrs)$", "Invalid consumption amount")
        self.fridge.consume_item(name, consumption)

    def current_status(self):
        self.fridge.current_status()

    def purchase_history(self):
        self.fridge.purchase_history()

    def search_item(self, keyword):
        return filter(lambda x: keyword in x, self.fridge._items.keys())

    def get_total_quantity(self):
        return sum(float(val.split()[0]) for val in self.fridge._items.values())
