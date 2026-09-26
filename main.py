"""this is a main.py for testing"""

import danaOneThree

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
    for i in range(1, 11):
        
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
            highConsDevice = danaOneThree.highestCons(device)

        severity = danaOneThree.severity(device, energyConsumption)
        
        if severity == "Normal":
            sumNormal +=1
        elif severity == "High":
            sumHigh +=1
        elif severity == "Critical":
            sumCritical +=1
        
        attention = danaOneThree.attention(device, energyConsumption)
        if attention == 1:
            sumAttention +=1
            
        cost = danaOneThree.cost(energyConsumption, rate)
        if cost is not None:
            totalCost += cost
        feedback = danaOneThree.feedback(device,energyConsumption)
        
    """task 6: report"""
    
    print("========== HomeSense Report ==========")
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