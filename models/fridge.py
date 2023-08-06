class Fridge:
    def __init__(self):
        self._items = {}
        self._history = []

    def insert_item(self, name, quantity):
        self._items[name] = quantity
        self._history.append(f"Added {quantity} of {name} to fridge.")

    def consume_item(self, name, consumption):
        if name not in self._items:
            raise ValueError(f"{name} not found in fridge")
        existing_quantity = self._items[name]
        new_quantity = float(existing_quantity.split()[
                             0]) - float(consumption.split()[0])
        unit = existing_quantity.split()[1]
        if new_quantity < 0:
            raise ValueError(
                f"Cannot consume {consumption} of {name}, only {existing_quantity} available")
        self._items[name] = f"{new_quantity:.2f} {unit}"
        self._history.append(f"Consumed {consumption} of {name} from fridge.")

    def current_status(self):
        print("Current status of fridge items:")
        for item, quantity in self._items.items():
            print(f"{item}: {quantity}")

    def purchase_history(self):
        print("Purchase history:")
        for event in self._history:
            print(event)
