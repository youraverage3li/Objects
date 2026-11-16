class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Order:
    def __init__(self, receipt,):
        self.receipt = receipt
    def calculate_taxes(self):
        taxes = 0
        for i in self.receipt:
            taxes += i.price * 0.07
        return taxes 
    def calculate_total(self):
        total = 0
        for i in self.receipt: 
            total += i.price 
        return total + self.calculate_taxes() 
    def add_item(self, item):
        self.receipt.append(item)
    def print_receipt(self):
        for item in self.receipt:
            print(f"{item.name}: ${item.price:.2f}")
        print(f"Taxes: ${self.calculate_taxes():.2f}")
        print(f"Total: ${self.calculate_total():.2f}")

def main():
   
   menu = [
       MenuItem("bagel", 3.00),
       MenuItem("burrito", 5.00),
       MenuItem("ramen", 1.50),
       MenuItem("gum", 0.50)
   ]
     
   order1 = Order([])
   order1.add_item(menu[1])
   order1.add_item(menu[1])
   order1.add_item(menu[3])

   total = order1.calculate_total()
   print("The total due is " + str(total))

   order1.print_receipt()
   

if __name__ == '__main__':
    main()
