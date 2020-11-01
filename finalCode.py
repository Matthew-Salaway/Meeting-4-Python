# Copy this code into your own repl. Click the navigation bar in the top left corner and go to My Repl.
# Click the New Repl on the left, create the repl, and paste the code. Or put into another IDE

# Today we will learn for loops/while loops, arrays (python lists), and tuples.

# Lets start with a review exercise. Lets make a function with the susd email algorithm.
# Start with the function name: susdEmail. There will be three parameters: firstName, lastName, and idNumber.
# Return the email as a string. (do not print)

def susdEmail(firstName, lastname, idNumber):
    firstInital = firstName[0]
    lastTwo = idNumber % 100
    email = firstInital + lastname + str(lastTwo) + "@susdgapps.org"
    return(email)

# Tuples: A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
student1 = ("Fernando", 3.67, True)   # Name, GPA, isOnlineSchool
print(student1)
print(student1[0])     # Prints the element at index 0
print(len(student1))   # returns the number of elements in tuple.

# Arrays: An array is a special variable, which can hold more than one value at a time. These values are elements.
# An array can hold many values under a single name, and you can access the values by referring to an index number.
car1 = "Ford"
car2 = "Tesla"
car3 = "BMW"

cars = ["Ford", "Tesla", "BMW"]

print(cars[0])    # Acess index with array[x], x being the index. Remember, index starts at 0

# Other array methods: https://www.w3schools.com/python/python_arrays.asp
print(len(cars))   # returns the number of elements in the array
cars.append(911)  # Adds another element the end of the array. # Python arrays allows different data types
cars.pop(2)           # Removes element at index (.remove() allows the element name to be specified)
print(cars)

# A loop is used to iterate over a sequence. This site explains it well
# While loops: https://www.w3schools.com/python/python_while_loops.asp
# For loops: https://www.w3schools.com/python/python_for_loops.asp


# Use the array of tuples down below called students and the susdEmail function to store all of the students email's as an array.
# Create a for-loop to traverse through the array of tuples. Then set each tuple up to become the parameter of
# the susdEmail function. Then store the returned email into an array called emails. Print emails
students = [("Matthew", "Salaway", 209832), ("Fred", "Lord", 988222), ("Debby", "Kujo", 998263), ("Skyler", "Ceptra", 762234)]
emails = []
for student in students:
    firstName = student[0]
    lastName = student[1]
    idNumber = student[2]
    email = susdEmail(firstName, lastName, idNumber)
    emails.append(email)
print(emails)
