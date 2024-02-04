def fahrenheit(temperature):
    C =  (5 / 9) * (temperature - 32)
    return C

temperature = float(input("temperature in fahrenheit: "))
celcium = fahrenheit(temperature)
print(f"{temperature} fahrenheit equalent to {celcium} celcium")



