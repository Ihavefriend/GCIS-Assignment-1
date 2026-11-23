from lost_item import LostItem

class LostFoundSystem:
    
    __slots__ = {"LostItemList"}
    
    def __init__(self):
        self.LostItemList = []
        
    def add_item(self,Item):
        if Item in self.LostItemList:
            return False
        self.LostItemList.append(Item)
        return True
        
    def search_item(self, item_id):
        for item in self.LostItemList:
            if item.get_ID() == item_id:
                return item
        return None
    
    def claim_item(self,item_id):
        item = self.search_item(item_id)
        if item:
            return item.mark_claimed()
        return False
    
    def display_items(self):
        for item in self.LostItemList:
            print(item)

    def save_items(self,filename):
        try:
            file = open(filename,"w")
            for item in self.LostItemList:
                line = f"{item.get_ID()}, {item.get_name()}, {item.get_category()}, {item.get_location()}, {item.get_status()}\n"
                file.write(line)
            
        except:
            print("Something has gone wrong...")
            return False
        file.close()
        return True
    
    def load_items(self,filename):
        try:
            file = open(filename)
            lines = file.readlines()
        except:
            print("Something has gone wrong...")
            return 0
        self.LostItemList = []
        for line in lines:
            stripped = line.strip()
            if not stripped: # not stripped returns true if value doesnt exist
                continue
            tempItem = [data.strip() for data in stripped.split(",")]
            id_str, name, category, location, status = tempItem
            item_ID = int(id_str)
            if item_ID <= 0 or not name or not category or not location:
                continue

            if status not in ("Lost", "Claimed"):
                continue
            try:
                item = LostItem(item_ID, name, category, location)
            except ValueError:
                continue
            if status == "Claimed":
                item.mark_claimed()

            if self.add_item(item):
                loaded_count += 1
        file.close()
        return loaded_count
        
            
