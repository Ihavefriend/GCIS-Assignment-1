from lost_found_system import LostFoundSystem
from lost_item import LostItem

def main():
    System = LostFoundSystem()
    while True:
        print("""
        1. Register Item
        2. Search Item
        3. Claim
        4. Display
        5. Save
        6. Load
        7. Exit
        """)
        userInput = int(input("Enter your choice: "))
        if userInput == 1:
            item_id = int(input("Enter item ID: "))
            if item_id is None:
                continue
            name = input("Enter item name: ")
            category = input("Enter item category: ")
            location = input("Enter location found: ")
            try:
                item = LostItem(item_id, name, category, location)
            except ValueError:
                print("Could not register item")
                continue  # Why is there a continue here
            if System.add_item(item):
                print("Item registered successfully! ")
            else:
                print(f"Error: Item ID {item_id} already exists!")

        elif userInput == 2:
            item_ID = int(input("Enter item ID: "))
            item = System.search_item(item_ID)
            if item:
                print("Item Found!")
                print(item)
            else:
                print("No item found with that ID.")
        elif userInput == 3:
            item_id = int(input("Enter item ID to claim: "))
            if System.search_item(item_id) is None:
                print("No item found with that ID.")
            elif System.claim_item(item_id):
                print(f"Item {item_id} successfully marked as Claimed!")
            else:
                print("Item is already claimed. No changes made")

        elif userInput == 4:
            System.display_items()

        elif userInput == 5:
            file = input("Enter file to save to: ")
            records = System.save_items(file)
            if records:
                print(f"{records} records saved successfully!")
            else: print("Error has occured.")

        elif userInput == 6:
            file = input("Enter file to load : ")
            records = System.load_items(file)
            if records:
                print(f"{records} records loaded successfully!")
            else: print("Error: File not found! 0 records loaded.")
            

        elif userInput == 7:
            print("Thank you for using Campus Lost & Found! Goodbye!")
            break
    
if __name__ == "__main__":
    main()