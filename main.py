class Device:
    def __init__(self, name, price, stock, warranty):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty_period = warranty

    def display_info(self):
        return f"{self.name} | Price: ${self.price} | Stock: {self.stock} | Warranty: {self.warranty_period} months"

    def __str__(self):
        return self.display_info()

    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)

    def is_available(self, amount):
        return self.stock >= amount

    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount
            return True
        return False


class Smartphone(Device):
    def __init__(self, name, price, stock, warranty, screen_size, battery_life):
        super().__init__(name, price, stock, warranty)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def display_info(self):
        base = super().display_info()
        return f"{base} | Screen: {self.screen_size}\" | Battery: {self.battery_life}h"

    def make_call(self): print(f"Calling from {self.name}...")
    def install_app(self): print(f"Installing app on {self.name}...")

class Laptop(Device):
    def __init__(self, name, price, stock, warranty, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def display_info(self):
        base = super().display_info()
        return f"{base} | RAM: {self.ram_size}GB | CPU: {self.processor_speed}GHz"

    def run_program(self): 
        print(f"Running software on {self.name}...")
    def use_keyboard(self): 
        print("Typing...")

class Tablet(Device):
    def __init__(self, name, price, stock, warranty, screen_resolution, weight):
        super().__init__(name, price, stock, warranty)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def display_info(self):
        base = super().display_info()
        return f"{base} | Res: {self.screen_resolution} | Weight: {self.weight}g"

    def browse_internet(self): 
        print(f"Browsing on {self.name}...")
    def use_touchscreen(self): 
        print("Swiping...")


class Cart:
    def __init__(self):
        self.items = [] 
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            print(f"Added {amount} x {device.name} to cart.")
        else:
            print(f"Insufficient stock for {device.name}!")

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        if not self.items:
            print("Cart is empty.")
            return
        for device, qty in self.items:
            print(f"- {device.name} (x{qty}): ${device.price * qty}")
        print(f"Total: ${self.total_price}")

    def checkout(self):
        if not self.items:
            print("Nothing to checkout!")
            return
        
        print("\n--- Receipt ---")
        for device, qty in self.items:
            device.reduce_stock(qty)
            print(f"Purchased: {qty} x {device.name}")
        print(f"Final Total: ${self.total_price}")
        self.items = []
        self.total_price = 0
        print("Thank you for your purchase!")
        
        
        
def main():
    inventory = [
        Smartphone("IPhone 15", 999, 10, 12, 6.1, 20),
        Smartphone("Galaxy S22 ultra", 850, 15, 24, 6.2, 22),
        Laptop("MacBook Air", 1200, 5, 12, 16, 3.2),
        Tablet("iPad Pro", 800, 12, 12, "2388x1668", 466),
    ]
    
    cart = Cart()

    while True:
        print("\n--- Electronic Store ---")
        print("1. Show Devices")
        print("2. Show Cart")
        print("3. Checkout")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            for i, dev in enumerate(inventory):
                print(f"{i+1}. {dev.display_info()}")
            
            sub_choice = input("\nEnter device # to add to cart (or 'b' to go back): ")
            if sub_choice.isdigit():
                idx = int(sub_choice) - 1
                if 0 <= idx < len(inventory):
                    qty = int(input(f"How many {inventory[idx].name}s? "))
                    cart.add_device(inventory[idx], qty)
        
        elif choice == '2':
            cart.print_items()
        
        elif choice == '3':
            cart.checkout()

        elif choice == '4':
            break

if __name__ == "__main__":
    main()