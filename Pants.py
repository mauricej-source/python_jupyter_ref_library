### TODO:
#   - code a Pants class with the following attributes
#   - color (string) eg 'red', 'yellow', 'orange'
#   - waist_size (integer) eg 8, 9, 10, 32, 33, 34
#   - length (integer) eg 27, 28, 29, 30, 31
#   - price (float) eg 9.28
#
### TODO: Declare the Pants Class 
### TODO: write an __init__ function to initialize the attributes
### TODO: write a change_price method:
#    Args:
#        new_price (float): the new price of the shirt
#    Returns:
#        None

### TODO: write a discount method:
#    Args:
#        discount (float): a decimal value for the discount. 
#            For example 0.05 for a 5% discount.
#
#    Returns:
#        float: the discounted price
#
class Pants:
    def __init__(self,color = 'red',waist_size=8,length=27,price=9.28):
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price
    
    def change_price(self,new_price):
        self.price = new_price
        
    def discount(self,percent_off):
        return self.price * (1-percent_off)