DO:
#   Code a SalesPerson class with the following attributes
#   - first_name (string), the first name of the salesperson
#   - last_name (string), the last name of the salesperson
#   - employee_id (int), the employee ID number like 5681923
#   - salary (float), the monthly salary of the employee
#   - pants_sold (list of Pants objects), 
#            pants that the salesperson has sold 
#   - total_sales (float), sum of sales of pants sold

### TODO: Declare the SalesPerson Class 
#        
### TODO: write an __init__ function to initialize the attributes
###    Input Args for the __init__ function:
#        first_name (str)
#        last_name (str)
#        employee_id (int)
# .      salary (float)
#
# You can initialize pants_sold as an empty list
# You can initialize total_sales to zero.
#
### TODO: write a sell_pants method:
#
#    This method receives a Pants object and appends
#    the object to the pants_sold attribute list
#
#    Args:
#        pants (Pants object): a pants object
#    Returns:
#        None
#
#            
### TODO: write a display_sales method:
#    
#    This method has no input or outputs. When this method 
#    is called, the code iterates through the pants_sold list
#    and prints out the characteristics of each pair of pants
#    line by line. The print out should look something like this
#
#   color: blue, waist_size: 34, length: 34, price: 10
#   color: red, waist_size: 36, length: 30, price: 14.15
#
#
### TODO: write a calculate_sales method:
#      This method calculates the total sales for the sales person.
#      The method should iterate through the pants_sold attribute list
#      and sum the prices of the pants sold. The sum should be stored
#      in the total_sales attribute and then return the total.
#      
#      Args:
#        None
#      Returns:
#        float: total sales
#
### TODO: write a calculate_commission method:
#
#   The salesperson receives a commission based on the total
#   sales of pants. The method receives a percentage, and then
#   calculate the total sales of pants based on the price,
#   and then returns the commission as (percentage * total sales)
#
#    Args:
#        percentage (float): comission percentage as a decimal
#
#    Returns:
#        float: total commission
#
#
###
class SalesPerson: 
    def __init__(self,first_name='Bob',last_name='Zumma',employee_id='00001',salary=25000.25,pants_sold=[],total_sales=0.00):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = (pants_sold)
        self.total_sales = total_sales

    def sell_pants(self,pants):
        self.pants_sold.append(pants)

    def display_sales(self):
        for index in range(len(self.pants_sold)):
            print('color: ' + (self.pants_sold[index]).color + ' ' +
                  'waist_size: ' + (self.pants_sold[index]).waist_size + ' ' +
                  'length: ' + (self.pants_sold[index]).length + ' ' +
                  'price: ' + (self.pants_sold[index]).price)
    def calculate_sales(self):
        total_sales = 0
        
        for index in range(len(self.pants_sold)):
            total_sales = total_sales + (self.pants_sold[index]).price
        
        return total_sales
    
    def calculate_commission(self,commision_percentage=0.00):
        total_commision = 0.00
        total_sales = round(self.calculate_sales(),2)
        total_commision = (total_sales)*commision_percentage
        return total_commision