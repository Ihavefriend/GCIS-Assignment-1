Device_Ranges = {
    "LED Light": (0.01, 0.10),
    "Television": (0.05, 0.50),
    "Refrigerator": (0.10, 1.50),
    "Washing Machine": (0.30, 2.50),
    "Air Conditioner": (0.50, 5.00),
}

"""
#########################################################################################################

                                        TASK 1 -  Analyzing single device readings

#########################################################################################################                                       
"""

def getDeviceRange(deviceName): 
    """ Task 1.1 - To make a function that returns the normal operating range of a device"""
    return Device_Ranges.get(deviceName,None) # Using .get() to return a default value incase the device is not present in the dictionary Device_Ranges

def getEnergyRating(deviceName,powerDraw):

    """ Task 1.2 - Write a function that returns if power draw is normal, high, or critical

        Normal - anything between 0 and 80% of max power draw
        High - power draw between 80% and 90%
        Critical - power draw above 90%
    
    """
    if powerDraw<0:
        return "Invalid powerDraw"
    
    deviceRange = getDeviceRange(deviceName)
    rangeMin,rangeMax = deviceRange

    if deviceRange is None:
        return "Unknown Device"
    elif powerDraw < rangeMax*0.8:
        return "Normal"
    elif powerDraw >= rangeMax*0.8 or powerDraw < rangeMax*0.9:
        return "High"
    elif powerDraw > rangeMax*0.9:
        return "Critical"

def attentionRequired(deviceName,powerDraw):
    """ Task 1.3 - This function returns true if status of device is high or critical, returns false if it is normal"""
    status = getEnergyRating(deviceName,powerDraw)
    return status in ["High","Critical"]

"""
#########################################################################################################

                                        TASK 2 -  Estimating Energy Costs

#########################################################################################################                                       
"""


def estimatedEnergyCost(powerDraw,energyCost):
    if powerDraw < 0 or energyCost < 0:
        return "Invalid Values Provided"
    return round(powerDraw*energyCost,2)


"""
#########################################################################################################

                                        TASK 3 -  Generating Smart Feedback

#########################################################################################################                                       
"""

def smartFeedback(deviceName,powerDraw):
    status = getEnergyRating(deviceName,powerDraw)
    if status == "Normal":
        return f"{deviceName} is operating efficiently within the normal range."
    elif status == "High":
        return f"Elevated usage on {deviceName} ({powerDraw:.2f} kWh). Check operating duration and settings."
    elif status == "Critical":
        return f"CRITICAL: Excessive consumption on {deviceName} ({powerDraw:.2f} kWh)! Inspect device immediately for faults or disconnect."


