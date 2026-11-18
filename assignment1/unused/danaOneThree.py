"""my interpretation of tasks 1-3 (aayans)"""

"""normal range, severity, and attention required: task 1"""
def operatingRange(device):
    if device == 1:
        minimum = 0.01
        maximum = 0.1
    elif device == 2:
        minimum = 0.05
        maximum = 0.5
    elif device == 3:
        minimum = 0.1
        maximum = 1.5
    elif device == 4:
        minimum = 0.3
        maximum = 2.5
    elif device == 5:
        minimum = 0.5
        maximum = 5.0
    else:
        print("Please select a valid device.")
        return None

    return minimum, maximum
    
def severity(device, energyConsumption):
# Normal: within the reference range
# High: up to 50% above the upper threshold
# Critical: more than 50% above the upper threshold

    normalRange = operatingRange(device)

    if normalRange == None:
        return

    minimum, maximum = normalRange
    
    if energyConsumption >= minimum and energyConsumption <= maximum:
        return "Normal"

    elif energyConsumption > maximum and energyConsumption <= maximum * 1.5:
        return "High"

    elif energyConsumption > maximum * 1.5:
        return "Critical"
        
def attention(device, energyConsumption):
    status = severity(device,energyConsumption)
    if status == "High" or status == "Critical":
        return 1
    else:
        return 0
    
"""task 2: cost"""
def cost(energyConsumption, rate):
    if energyConsumption < 0 or rate < 0:
        print("Please enter valid values.")
        return None
    else:
        return energyConsumption * rate

"""task 3: feedback"""
def feedback(device,energyConsumption):
    status = severity(device,energyConsumption)
    
    if status == "Normal":
        return "Operating efficiently within the normal range."
    elif status == "High":
        return "Check the operating duration and temperature settings"
    elif status == "Critical":
        return "CRITICAL: Excessive consumption! Inspect device immediately for faults or disconnect."
    
def highestCons(device): #EXTRA FUNCTION FROM DANA
    if device == 1:
        return "LED Light"
    elif device == 2:
        return "Television"
    elif device == 3:
        return "Refrigerator"
    elif device == 4:
        return "Washing Machine"
    elif device == 5:
        return "Air Conditioner"