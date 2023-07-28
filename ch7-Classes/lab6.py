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

if __name__ == "__main__":
# Solution
    # TASK: Create VendingMachine object
    my_vend = VendingMachine()
    # TASK: Purchase input number of drinks
    my_vend.purchase(int(input()))
    # TASK: Restock input number of bottles
    my_vend.restock(int(input()))
    # TASK: Report inventory
    my_vend.report()
# End solution