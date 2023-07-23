# Allows user to order for either delivery or click-and-collect
import time

print("Would you like to order for click-and-collect or delivery?")
time.sleep(2.5)
print("")
print("Enter 1 for Click-and-collect")
print("Enter 2 for Delivery ($9.00 surcharge)")
print("Enter 0 to exit the program")

while True:
    try:
        ordtype = int(input("Enter number here > "))

        if ordtype == 0:
            print("Goodbye~!")
            time.sleep(3) # Replace with program exit function
            exit()

        elif ordtype == 1:
            print("Pick-up!") # Replace with pickupinfo_v*
            break

        elif ordtype == 2:
            print("Delivery!") # Replace with deliveryinfo_v*
            break
        

        else:
            print("")
            print("Invalid number! Enter either 1 or 2!")
    
    except ValueError:
        print("")
        print("Invalid input! Please enter either 1 or 2")

# Add connection to userinfo later