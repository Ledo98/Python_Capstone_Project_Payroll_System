
def calculate_bonus(base_salary, performance_rating):
    base_salary = float(base_salary)
    performance_rating = int(performance_rating)

    if performance_rating == 5 :
       bonus_amount= (20/100) * base_salary
       print ("Excellent performance")
    elif performance_rating == 4 or performance_rating == 3 :
      bonus_amount= (10/100) * base_salary
      print ("Good performance")
    else :
      bonus_amount= (0/100) * base_salary
      print ("Needs improvement")
    return bonus_amount


def calculate_tax(gross_salary) :
  gross_salary = float(gross_salary)

  if gross_salary > 7000 :
    tax_amount = (15/100) * gross_salary

  elif 3000 < gross_salary < 7000 :
    tax_amount = (10/100) * gross_salary

  else :
    tax_amount = (0/100) * gross_salary
  return tax_amount

def main_hr_app():

  print ("**********  Welcome TO MOhamed Waleed First Project  **********")

  employees_name= str(input("Enter Your Name :"))
  Department = str(input("Enter Your Department :"))
  base_salary = float(input("Enter Your Salary :"))
  performance_rating = int(input("Enter Performance Rate :"))
  
  if  base_salary < 0  :
    print("salary cannot be negative ")
    return
  if performance_rating < 1 or performance_rating > 5 :
    print("Please ensure rating is between 1 and 5 ")
    return 

  bonus = calculate_bonus(base_salary, performance_rating)
  gross_salary = base_salary + bonus
  tax = calculate_tax(gross_salary)
  net_salary = gross_salary - tax
  
  print("---------------------------------------------------------------------")
  

  print("Employee Name:", employees_name)
  print("Department:", Department)
  print("Base Salary:", base_salary)
  print("Performance Rating:", performance_rating)
  print("Bonus Amount:", bonus )
  print("Gross Salary:", gross_salary)
  print("Tax Amount:", tax)
  print("Net Salary:", net_salary)


main_hr_app()

     
  
