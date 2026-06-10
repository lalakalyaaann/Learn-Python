try:
    a=int(input("Enter a number : "))
    b=7/a
    print(b)
except:
    print("Error in input. Please enter correct number")

list=[1,2,3,4,5]
for i in list:
    print(i)


#finally block
try:
    a=int(input("Enter a number : "))
    b=7/a
    print(b)
except:
    print("Error in input. Please enter correct number")

finally:
    print("This code will always execute.")


#more descriptive exceptions
try:
    a=int(input("Enter a number : "))
    b=7/a
    print(b)
except Exception as e:
    print("Error in input. Please enter correct number.",e)
finally:
    print("This code will always execute.")

try:
    a=int(input("Enter a number : "))
    b=7/a
    print(b)
except ValueError as e:
    print("Error in input. Please enter correct number.",e)
except ZeroDivisionError as e:
    print("Error in input. Please enter correct number.",e)
except Exception as e:
    print("Error in input. Please enter correct number.",e)
finally:
    print("This code will always execute.")