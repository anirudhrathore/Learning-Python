


try:
    answer = 10/0
    number = int(input("Enter a number : "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
# We can also print out the actual error
#except ZeroDivisionError as err:
 #   print(err)
except ValueError:
    print("Invalid Input")