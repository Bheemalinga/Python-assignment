# python assignment
# Session 1 / 2
# input / output / if conditions / loops

''' 1. Accept Empid,EmpName,Monthly_Salary,Tot_Deductions, Tot_Allowances       and Display Employee Name and Salary in hand'''
'''
emp = int(input("Enter Employee id: "))
name = input("Enter Employee name: ")
salary = int(input("Enter Employee salary: "))
deductions = int(input("Enter Employee deductions: "))
allowances = int(input("Enter Employee allowances: "))
salary_in_hand = salary + allowances - deductions
print("Employee Name: ", name)
print("Employee Salary in hand: ", salary_in_hand)
'''




'''
1. Accept integers from User till Users Choice and do the Following: 
1. Sum of all Integers
2. Average of all Integers
3. Maximum Integer from all
4. Minimum Integer from all
'''

''' 
numbers = []
while True:
    n = input("Enter a number or type 'quit' to exit: ")
    if n.upper() == "QUIT":
        break
    numbers.append(int(n))
    print("Sum of all integers: ", sum(numbers))
    print("Average of all integers: ", sum(numbers)/len(numbers))
    print("Maximum Integer: ", max(numbers))
    print("Minimum Integer: ", min(numbers))
'''





''' 
 2. Accept a String from User an do the following : 
 1. Find the Length
 2. Display String in reverse        
 2. Display every alternate Character in Upper Case        
 3. Find out No of Vowels in the String        
 4. Accept Username and Date of Birth (dd-mon-yy) from User          
 Create a Password String which will be combination of           
 1st 4 letters of username and last 2digits of Date of Birth followed by $ sign
 5. Encrypt the String and return Encrypted String(Assume your Algorithm)
'''

''' 
accepting_string = input("Enter a string: ")
print("Length of the string: ", len(accepting_string))
print("String in reverse: ", accepting_string[::-1])
print("Every alternate character in Upper Case: ", accepting_string[::2].upper())
vowels = "aeiou"
count = 0
for i in accepting_string:
    if i in vowels:
        count += 1
print("Number of vowels in the string: ", count)
username = input("Enter username: ")
dob = input("Enter date of birth(dd-mon-yy): ")
password = username[:4] + dob[-2:] + "$"
print("Password: ", password)
sring_encryption = ""
for i in password:
    sring_encryption += chr(ord(i)+2)
print("Encrypted string: ", sring_encryption)
'''






''' 
 3. Write Python Program to do the following : 
   1. Display Area of Circle, Parallelogram
'''

''' 
radius_of_circle = int(input("Enter radius of circle: "))
area_of_circle = 3.14 * radius_of_circle * radius_of_circle
print("Area of circle: ", area_of_circle)

base = int(input("Enter base of parallelogram: "))
height = int(input("Enter height of parallelogram: "))
area_of_parallelogram = base * height
print("Area of parallelogram: ", area_of_parallelogram)
'''







''' 
 4. Accept Integer and find Square root of Integer
'''
'''
integer = int(input("Enter an integer: "))
square_root = integer ** 0.5
# because square root = power 1/2 = power 0.5
print("Square root of integer: ", square_root)
'''







''' 
B. Session 3 / 4
List / Tuples / Dictionary / Sets
'''

'''
1. Create a List for the following :
 a. Accept Fruits Name and their price(per kg)
  b. Fruits Name should be at odd index position in the List.
      Price at even index position 
'''
'''
fruits = []
while True:
    fruit = input("Enter fruit name or type 'quit' to exit: ")
    if fruit.upper() == "QUIT":
        break
    price = int(input("Enter price of fruit: "))
    fruits.append(fruit)
    fruits.append(price)

print("Fruits and their prices: ", fruits)
'''







'''
2. Customer will buy fruits from you (Show him the Fruits Menu)
 Write a Program to 
 a. Calculate Total Price of Fruits Bought (Assume price for 1 kg ) 
 b. Add New Fruits in the List
 c. Show Total Fruits in the List
'''
'''
fruits = {
    'Apple': 30,
    'Banana': 10,
    'Orange': 20,
    'Grapes': 40,
    'Mango': 50
}

print("Fruits Menu:")
for fruit, price in fruits.items():
    print("{}: ${} per kg".format(fruit, price))

fruit_name = input("Enter the fruit you want to buy: ")
quantity = float(input("Enter the quantity in kg: "))

if fruit_name in fruits:
    total_price = fruits[fruit_name] * quantity
    print("Total price for {} kg of {}: ${}".format(quantity, fruit_name, total_price))
else:
    print("Fruit not available.")

new_fruit = input("Enter a new fruit to add: ")
new_price = float(input("Enter the price for {} per kg: ".format(new_fruit)))

if new_fruit not in fruits:
    fruits[new_fruit] = new_price
    print(f"{new_fruit} has been added to the list.")
else:
    print(f"{new_fruit} is already in the list.")

total_fruits = len(fruits)
print(f"Total fruits in the list: {total_fruits}")
'''












'''
3. Create Foll. Information in the Tuple (atleast 5 Employees)
 1. EmpId - Phone Numbers (One Employee can have Multiple Numbers )
  2. Accept Empid from User.
  Display his Numbers only if he exists in the Database(Tuple)
  Display App. Message if not present
  3. Update Employee phone Number
     Accept Empid from User
     Check whether he / she Exists 
     Accept New Phone Number
     Update
     Display Appropriate Message for any task
'''
'''
Foll = {1: [1234456,8932487], 2:[847978543], 3:[764363745,829389352,29075], 4:[2323758], 5:[3945732583]}
Empid = int(input("Enter Employee id: "))
if Empid in Foll:
    print("Employee numbers: ", Foll[Empid])
else:
    print("Employee not found")
# Update Employee phone Number
Empid = int(input("Enter Employee id: "))
if Empid in Foll:
    new_number = int(input("Enter new phone number: "))
    Foll[Empid].append(new_number)
    print("Phone number updated successfully.")
'''








"""
4. Store the Following info in Dictionary
Department Name and their Employee Names
Note : One Department can have multiple Employees
Perform the Following Operations : 
1. Add a New Department Name and Employees in that Department 
    If a New Department Name doesnot Exists.add()
2. Accept Dept Name from User and List all Employees 
    If Dept Name Exists in the Database.add()
3. Add a New Employee in Existing Department.
4. Delete Existing Employee From Department
"""
"""
company = {hr : ["aperson","yperson"], it : ['suresh','zperson','naresh'], finance:['qperson']}
print("1. Add a New Department Name and Employees in that Department")
dept_name = input("Enter department name: ")
if dept_name not in company:
    employees = input("Enter employees in the department: ").split()
    company[dept_name] = employees
    print("Department added successfully.")
else:
    print("Department already exists.")

print("2. Enter Dept Name for List of all Employees")
dept_name = input("Enter department name: ")
if dept_name in company:
    print("Employees in the department: ", company[dept_name])
else:
    print("Department not found.")

print("3. Add a New Employee in Existing Department")
dept_name = input("Enter department name: ")
if dept_name in company:
    employee = input("Enter employee name: ")
    company[dept_name].append(employee)
    print("Employee added successfully.")
else:
    print("Department not found.")

print("4. Delete Existing Employee From Department")
dept_name = input("Enter department name: ")
if dept_name in company:
    employee = input("Enter employee name: ")
    if employee in company[dept_name]:
        company[dept_name].remove(employee)
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")
else:
    print("Department not found.")
"""











'''
5. Create Following two Sets
    1. Fruit_Salesman1
    2. Fruit_Salesman2
    Accept the Fruits Sold by Both Salesman
    Perform the Following Operations
    1. Display common fruits with both Salesman
    2. List extra fruits with both Salesman
    3. List all fruits sold by both Salesman
'''
'''
salesman1 = {"apple", "banana", "orange", "grapes", "mango"}
salesman2 = {"apple", "banana", "kiwi", "papaya", "watermelon"}

common_fruits = salesman1.intersection(salesman2)
print("Common fruits: ", common_fruits)

extra_fruits_salesman1 = salesman1.difference(salesman2)
print("Extra fruits sold by salesman1: ", extra_fruits_salesman1)
extra_fruits_salesman2 = salesman2.difference(salesman1)
print("Extra fruits sold by salesman2: ", extra_fruits_salesman2)

all_fruits = salesman1.union(salesman2)
print("All fruits sold by both salesman: ", all_fruits)
'''










'''
 
'''
