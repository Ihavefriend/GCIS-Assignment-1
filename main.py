import danaOneThree

def main():
    
    print("1- LED Light\n2- Television\n3- Refrigerator\n4- Washing Machine\n5- Air Conditioner")
    
    device = int(input("Choose your device (1, 2, 3, 4, 5): "))
    energyConsumption = float(input("Please enter your energy consumption in kWh: "))

    severity = danaOneThree.severity(device, energyConsumption)
    
if __name__ == "__main__":
    main()