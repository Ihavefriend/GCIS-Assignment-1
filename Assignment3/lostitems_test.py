import pytest
from lost_item import LostItem

print("Dana's TESTS")

def test_danaInvalidID():
    # setup
    itemID = 0
    expected = False

    # invoke
    actual = LostItem(itemID, "Laptop", "Electronics", "Library")

    # analyze
    assert actual == expected


def test_danaEmptyString():
    # setup
    name = "   "
    expected = False

    # invoke
    actual = LostItem(101, name, "Electronics", "Library")

    # analyze
    assert actual == expected


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
    expected = False

    # invoke
    actual = LostItem(ID, "Calculator", "Electronics", "Room 204")

    # analyze
    assert actual == expected


print("AI's TESTS")


def test_aiStringID():
    # setup
    ID = "101"
    expected = False

    # invoke
    actual = LostItem(ID, "Laptop", "Electronics", "Library")

    # analyze
    assert actual == expected


def test_aiEmptyCategory():
    # setup
    category = ""
    expected = False

    # invoke
    actual = LostItem(102, "Laptop", category, "Library")

    # analyze
    assert actual == expected


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
    expected = False

    # invoke
    actual = LostItem(ID, "Laptop", "Electronics", "Library")

    # analyze
    assert actual == expected
    
def test_aiEmptyLocation():
    # setup
    location = ""
    expected = False

    # invoke
    actual = LostItem(103, "Calculator", "Electronics", location)

    # analyze
    assert actual == expected