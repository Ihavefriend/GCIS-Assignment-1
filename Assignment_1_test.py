import pytest


from Assignment_1 import * 


def test_normal_reading():
    expected = "Normal"
    actual = getSeverity(1, 0.05)
    assert expected == actual 


def test_boundary_limit_reading():
    expected = "Normal"
    actual = getSeverity(1, 0.08)
    assert expected == actual

def test_low_reading():
    expected = "Low"
    actual = getSeverity(1,0.00001)
    assert expected == actual
def test_high_reading():
    expected = "High"
    actual = getSeverity(2, 0.6)
    assert expected == actual


def test_critical_reading():
    expected = "Critical"
    actual = getSeverity(3, 2.6)
    assert expected == actual


def test_energy_cost_calculation():
    expected = 1.20
    actual = getCost(4.0, 0.30)
    assert expected == actual


def test_attention_decision():
    expected = True
    actual = getAttention(4, 10)
    assert expected == actual


def test_smart_feedback_high():
    expected = True
    actual = "HIGH" in getFeedback(2, 0.7)
    assert expected == actual


def test_smart_feedback_critical():
    expected = True
    actual = "CRITICAL" in getFeedback(5, 15)
    assert expected == actual

