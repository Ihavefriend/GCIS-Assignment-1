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
            pass
        elif userInput == 2:
            pass
        elif userInput == 3:
            pass
        elif userInput == 4:
            pass
        elif userInput == 5:
            pass
        elif userInput == 6:
            pass
        elif userInput == 7:
            break
    
if __name__ == "__main__":
    main()