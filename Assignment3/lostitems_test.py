import pytest
from lost_item import LostItem

print("Dana's TESTS")

def test_danaInvalidID():
    # setup
    itemID = 0

    with pytest.raises(ValueError):
        LostItem(itemID, "Laptop", "Electronics", "Library")


def test_danaEmptyString():
    # setup
    name = "   "

    with pytest.raises(ValueError):
        LostItem(101, name, "Electronics", "Library")


def test_danaSameID():
    # setup
    item1 = LostItem(101, "Laptop", "Electronics", "Library")
    item2 = LostItem(101, "Water Bottle", "Personal", "Cafeteria")
    expected = True

    # invoke
    actual = item1 == item2

    # analyze
    assert actual == expected


def test_danaNegID():
    # setup
    ID = -50


    with pytest.raises(ValueError):
        LostItem(ID, "Calculator", "Electronics", "Room 204")


print("AI's TESTS")


def test_aiStringID():
    # setup
    ID = "101"

    with pytest.raises(ValueError):
        LostItem(ID, "Laptop", "Electronics", "Library")


def test_aiEmptyCategory():
    # setup
    category = ""
    expected = False

    with pytest.raises(ValueError):
        LostItem(102, "Laptop", category, "Library")


def test_aiDifferentID():
    # setup
    item1 = LostItem(101, "Laptop", "Electronics", "Library")
    item2 = LostItem(102, "Laptop", "Electronics", "Library")
    expected = False

    # invoke
    actual = item1 == item2

    # analyze
    assert actual == expected


def test_aiFloatID():
    # setup
    ID = 101.5

    with pytest.raises(ValueError):
        LostItem(ID, "Laptop", "Electronics", "Library")
    
def test_aiEmptyLocation():
    # setup
    location = ""
    with pytest.raises(ValueError):
        LostItem(103, "Calculator", "Electronics", location)