class LostItem:
    
    __slots__ = ["__ID","__name","__category","__location","__status"]
    
    def __init__(self, ID, name, category, location):
        if not(type(ID) == int) or ID<=0:
            raise ValueError("Enter a valid ID")
        
        if not(name.strip() and category.strip() and location.strip()): #if this are unable to be stripped because theyre empty,
            raise ValueError("Do not keep name, category, or location empty")
        
        self.__ID = ID
        self.__name = name
        self.__category = category
        self.__location = location
        self.__status = "Lost" #lost by default as per assignment

    def get_ID(self):
        return self.__ID

    def get_name(self):
        return self.__name

    def get_category(self):
        return self.__category

    def get_location(self):
        return self.__location

    def get_status(self):
        return self.__status
    
    def __str__(self):
        return f"{self.__ID} | {self.__name} | {self.__category} | {self.__location} | {self.__status}"
    
    def __eq__(self,other):
        if type(self) == type(other):
            return self.__ID == other.__ID
        else: return NotImplemented
    
    def mark_claimed(self):
        if self.__status == "Lost":
            self.__status = "Claimed"
            return True
        if self.__status == "Claimed":
            return False