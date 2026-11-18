from lost_item import LostItem

class LostFoundSystem:
    __slots__ = {"LostItemList"}
    def __init__(self):
        self.LostItemList = []
    def add_item(self,Item):
        if Item in self.LostItemList:
            return False
        self.LostItemList.append(Item)
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
