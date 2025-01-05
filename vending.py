import pyttsx3
class VendingMachine:
    def __init__(self):
       self.speaker = pyttsx3.init()
       self.items = {
            "A1": {"name": "Potato Chips", "price": 1.50, "category": "Snacks", "stock": 5},
            "A2": {"name": "Ice Tea", "price": 2.00, "category": "Drinks", "stock": 5},
            "B1": {"name": "Chocolate Bar", "price": 1.50, "category": "Snacks", "stock": 5},
            "B2": {"name": "Water Bottle", "price": 0.75, "category": "Drinks", "stock": 5},
            "C1": {"name": "Strawberry Milk", "price": 1.75, "category": "Drinks", "stock": 5},
            "C2": {"name": "Gummy Bears", "price": 2.50, "category": "Snacks", "stock": 5},
            "D1": {"name": "Low-Fat Cookies", "price": 1.50, "category": "Healthy", "stock": 5},
            "D2": {"name": "Granola Bar", "price": 1.25, "category": "Healthy", "stock": 5},
            "E1": {"name": "Dried Fruits", "price": 2.00, "category": "Healthy", "stock": 5},
            "E2": {"name": "Chocolate Milk", "price": 1.75, "category": "Drink", "stock": 5},
        }
    def speak(self, text):
        self.speaker.say(text)
        self.speaker.runAndWait()       

    def displayed_items(self):
        print ("\n Welcome to Matthew's Vending Machine!!!")
        self.speak("Welcome to matthe's vending machine!")
        print("\nAvailable items:")
        self.speak("Here are the available items")
        for code, item in self.items.items():
            stock_status = f"(Stock: {item['stock']})" if item['stock'] > 0 else "(Out of Stock)"
            print(f"Code: {code} | {item['name']} | ${item['price']:.2f} ({item['category']}) {stock_status}")
            
            
            



    def item_select(self):
        while True:
            code = input("\nEnter the item code: ").upper()
            
            if code in self.items:
                item = self.items[code]
                if item['stock'] > 0:
                    print(f"Selected: {item['name']} (${item['price']:.2f})")
                    self.speak(f"You selected {item['name']}. It costs ${item['price']:.2f}.")
                    if self.processing_payment(item):
                        item['stock'] -= 1
                    break
                else:
                    print("Sorry but this item is currently out of stock.")
                    self.speak("Sorry but this item is currently out of stock.")
                    break
            else:
                print("The Code is Invalid. Please try enter a valid code.")
                self.speak("The Code is Invalid. Please try enter a valid code.")

    def processing_payment(self, item):
        total = item['price']
        inserted = 0
        while inserted < total:
            try:
                coin = float(input(f"Insert money ($ remaining: {total - inserted:.2f}): "))
                self.speak(f"Insert money ($ remaining: {total - inserted:.2f}): ")
                if coin > 0:
                    inserted += coin
                    print(f"Total inserted: ${inserted:.2f}")
                    self.speak(f"Total inserted is ${inserted:.2f}.")
                else:
                    print("Please insert a positive amount.")
                    self.speak("Please insert a positive amount.")
            except ValueError:
                print("The input is unvalid. Please insert an valid money.")
                self.speak("The input is unvalid. Please insert an valid money.")

        if inserted >= total:
            change = inserted - total
            print(f"Dispensing {item['name']}.")
            self.speak(f"Dispensing {item['name']}.")
            if change > 0:
                print(f"Returning change: ${change:.2f}")
                self.speak(f"Returning change of ${change:.2f}.")
            return True
        else:
            print("The funds is lacking. The Transaction will becancelled.")
            self.speak("The funds is lacking. The Transaction will becancelled.")
            return False

    def start(self):
        while True:
            self.displayed_items()
            self.item_select()
            self.speak("Would you buy another item?")
            again = input("Would you buy another item? (yes/no): ").strip().lower()
            
            if again != "yes":
                print("Thank you for using Matthew's Vending Machine!")
                self.speak(" Thank you for using the vending machine.")
                break

if __name__ == "__main__":
    VendingMachine().start()
