"""Switch Control (If-Else)

Write a Python program to simulate the operation of a switch in a circuit. 
If the input voltage is greater than or equal to 3V, the switch turns on; otherwise, it turns off."""
voltage=int(input("Enter the input voltage: "))
if voltage>=3:
    print("Switch is ON")
else:
    print("Switch is OFF")
#using fuctions
def switch_control(voltage):
    if voltage>=3:
        return "Switch is ON"
    else:
        return "Switch is OFF"
voltage=int(input("Enter the input voltage: "))
print(switch_control(voltage))
"""
Power System Check (If-Else)

Implement a Python program that checks if the total power in a system exceeds the safe limit. 
If it does, print "Power overload"; otherwise, print "Power within limit"."""
"""The safe power limit for single-phase and three-phase connections depends on various factors,
including voltage, current capacity, and regional regulations.
- Single-phase power: Typically used in homes and small businesses, 
single-phase connections in India operate at 230V with a frequency of 50Hz. 
The maximum load capacity can vary, but residential connections often handle up to 7.5 kW.
- Three-phase power: Used for industrial and commercial applications, three-phase connections in India operate
at 415V with a frequency of 50Hz. The maximum load capacity can go much higher, often exceeding 100 kW, 
depending on the infrastructure and transformer capacity.

For this example, let's assume a safe limit of 10 kW for single-phase connections and
    """
power=int(input("Enter the total power: "))
safelimit=10
if power>safelimit:
    print("The power is overloaded.")
else:
    print("Power is within the limits.")
#using functions
def power_check(power,safelimit):
    if power>safelimit:
        return "The power is overloaded."
    else:
        return "Power is within the limits."
power_check(int(input("Enter the total power: ")),10)
"""
Circuit Breaker Status (If-Else)

Write a Python program to simulate the status of a circuit breaker.
If the current exceeds 10A, print "Breaker tripped"; otherwise, print "Circuit normal".
"""
current=int(input("Enter the current: "))
if current>10:
    print("Breaker tripped")
else:
    print("Circuit normal.")
#using functions
def breaker_status(current):
    if current>10:
        return "Breaker tripped"
    else:
        return "Circuit normal"
print(breaker_status(int(input("Enter the current: "))))
"""
Motor Protection (If-Else)

Implement a program that checks if the motor's operating conditions are safe. 
If the current exceeds the maximum limit (e.g., 15A), print "Motor Overload"; otherwise,
print "Motor running safely".
"""
CURRENT=int(input("Enter the current: "))
MAX_CURRENT=15
if CURRENT>MAX_CURRENT:
    print("Motor Overload")
else:
    print("Motor running Safely!!")
#using functions
def motor_operation(current,Max_current):
    if current>Max_current:
        return "Motor Overload"
    else:
        return "Motor running Safely!!"
print(motor_operation(int(input("Enter the current: ")),15))
"""
Create a program to check if the temperature of an electrical component exceeds 75°C. Print "Overheating" if true, otherwise "Temperature Normal".
"""
    