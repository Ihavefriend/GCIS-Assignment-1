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
    
def getSeverity(device, energyConsumption):
# Normal: within the reference range
# High: up to 50% above the upper threshold
# Critical: more than 50% above the upper threshold

    normalRange = operatingRange(device)

    if normalRange == None:
        return

    minimum, maximum = normalRange
    if energyConsumption < minimum:
        return "Low"
    elif energyConsumption >= minimum and energyConsumption <= maximum:
        return "Normal"

    elif energyConsumption > maximum and energyConsumption <= maximum * 1.5:
        return "High"

    elif energyConsumption > maximum * 1.5:
        return "Critical"
        
def getAttention(device, energyConsumption):
    status = getSeverity(device,energyConsumption)
    if status == "High" or status == "Critical":
        return 1
    else:
        return 0
    
"""task 2: cost"""
def getCost(energyConsumption, rate):
    if energyConsumption < 0 or rate < 0:
        print("Please enter valid values.")
        return None
    else:
        return energyConsumption * rate

"""task 3: feedback"""
def getFeedback(device,energyConsumption):
    status = getSeverity(device,energyConsumption)
    if status == "Low":
        return "Operating below recommended range"
    elif status == "Normal":
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


def main():
        
    sumDevices = 0
    sumNormal = 0
    sumHigh = 0
    sumCritical = 0
    sumAttention = 0
    totalEnergy = 0.0
    totalCost = 0.0
    highCons = 0.0
    highConsDevice = ""
    rate = 0.3 # AED / kWh, constant
    
    print("1- LED Light\n2- Television\n3- Refrigerator\n4- Washing Machine\n5- Air Conditioner")

    """task 4"""
    while sumDevices<2:  # Set at 2 for testing
        
        """all of the below is task 5"""
        
        device = int(input("Choose your device (1, 2, 3, 4, 5): "))

        if device < 1 or device > 5:
            print("Please select a valid device.")
            continue
        
        energyConsumption = float(input("Please enter your energy consumption in kWh: "))
        if energyConsumption < 0:
            print("Please enter valid values.")
            continue
        sumDevices +=1
        totalEnergy += energyConsumption
        
        if energyConsumption > highCons:
            highCons = energyConsumption
            highConsDevice = highestCons(device)

        severity = getSeverity(device, energyConsumption)
        
        if severity == "Normal":
            sumNormal +=1
        elif severity == "High":
            sumHigh +=1
        elif severity == "Critical":
            sumCritical +=1
        
        attention = getAttention(device, energyConsumption)
        if attention == 1:
            sumAttention +=1
            
        cost = getCost(energyConsumption, rate)
        if cost is not None:
            totalCost += cost
        feedback = getFeedback(device,energyConsumption)

        print("\n",feedback,"\n")
    """task 6: report"""
    
    print("\n========== HomeSense Report ==========")
    print("Readings analyzed:", sumDevices)
    print("\nNormal:", sumNormal)
    print("High:", sumHigh)
    print("Critical:", sumCritical)
    print("\nReadings requiring attention:", sumAttention)
    print("\nTotal energy:", totalEnergy, "kWh")
    print("Estimated cost: AED", totalCost)
    print("Highest consumption:")
    print(highConsDevice,"-",highCons, "kWh") 
    
if __name__ == "__main__":
    main()