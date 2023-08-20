#   7.16 LAB: Vending machine
#   Given two integers as user inputs that represent the number of drinks to buy and the number of bottles to restock, create a VendingMachine object that performs the following operations:
#   
#   Purchases input number of drinks
#   Restocks input number of bottles
#   Reports inventory
#   A VendingMachine's initial inventory is 20 drinks.
#   
#   Ex: If the input is:
#   
#   5
#   2
#   the output is:
#   
#   Inventory: 17 bottles

class VendingMachine:
    def __init__(self):
        self.bottles = 20
        
    def purchase(self, amount):
        self.bottles = self.bottles - amount
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print(f'Inventory: {self.bottles} bottles')
# Solution
if __name__ == "__main__":
    # TASK: Create VendingMachine object
    my_vend = VendingMachine()
    # TASK: Purchase input number of drinks
    my_vend.purchase(int(input()))
    # TASK: Restock input number of bottles
    my_vend.restock(int(input()))
    # TASK: Report inventory
    my_vend.report()
# End solution