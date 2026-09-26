import pytest


from assignment import (
    getDeviceRange,
    getEnergyRating,
    attentionRequired,
    estimatedEnergyCost,
    smartFeedback,
)

# Test Function 1
def test_normal_reading():
    assert getEnergyRating("LED Light", 0.05) == "Normal"

# Test Function 2
def test_boundary_limit_reading():
    assert getEnergyRating("LED Light", 0.08) == "Normal"

# Test Function 3
def test_high_reading():
    assert getEnergyRating("Television", 0.43) == "High"

# Test Function 4
def test_critical_reading():
    assert getEnergyRating("Refrigerator", 1.40) == "Critical"

# Test Function 5
def test_energy_cost_calculation():
    assert estimatedEnergyCost(4.0, 0.30) == 1.20

# Test Function 6
def test_attention_decision():
    assert attentionRequired("Washing Machine", 2.40) is True

# Test Function 7
def test_invalid_unusual_input():
    assert getEnergyRating("LED Light", -0.05) == "Invalid powerDraw"

# Test Function 8
def test_smart_feedback():
    feedback = smartFeedback("Air Conditioner", 4.8)
    assert "CRITICAL" in feedback
