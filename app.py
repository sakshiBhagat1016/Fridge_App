from models.fridge import Fridge
from services.fridge_service import FridgeService
from functools import partial


class FridgeApp:
    def __init__(self):
        self.fridge = Fridge()
        self.fridge_service = FridgeService(self.fridge)

    def run(self):
        while True:
            self._display_menu()
            choice = self._get_user_choice()
            self._perform_action(choice)

    def _display_menu(self):
        print("\n")
        print("\n")
        print("Welcome to the Fridge")
        print("Please choose an option:")
        print("1. Insert item")
        print("2. Consume item")
        print("3. View current status")
        print("4. View purchase history")
        print("5. Search for an item")
        print("6. Get total quantity")
        print("7. Exit")
        print("\n")

    def _get_user_choice(self):
        choice = input()
        if not choice.isdigit() or int(choice) not in range(1, 8):
            print("Invalid choice, please try again")
            return self._get_user_choice()
        return int(choice)

    def _perform_action(self, choice):
        if choice == 1:
            name = input("Enter item name: ")
            quantity = input("Enter quantity (e.g. 1 Kg or 500 ml): ")
            self.fridge_service.insert_item(name, quantity)
        elif choice == 2:
            name = input("Enter item name: ")
            consumption = input("Enter consumption amount (e.g. 0.5 Ltrs): ")
            self.fridge_service.consume_item(name, consumption)
        elif choice == 3:
            self.fridge_service.current_status()
        elif choice == 4:
            self.fridge_service.purchase_history()
        elif choice == 5:
            keyword = input("Enter search keyword: ")
            search_result = self.fridge_service.search_item(keyword)
            for item in search_result:
                print(item)
        elif choice == 6:
            total_quantity = self.fridge_service.get_total_quantity()
            print(f"Total quantity in fridge: {total_quantity} Ltrs/Kg")
        elif choice == 7:
            print("Thank you for using Fridge App!")
            exit()


if __name__ == "__main__":
    app = FridgeApp()
    app.run()
