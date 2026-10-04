import pytest


from Assignment_1 import * 


def test_normal_reading():
    assert getSeverity(1, 0.05) == "Normal"


def test_boundary_limit_reading():
    assert getSeverity(1, 0.08) == "Normal"


def test_high_reading():
    assert getSeverity(2, 0.6) == "High"


def test_critical_reading():
    assert getSeverity(3, 2.6) == "Critical"


def test_energy_cost_calculation():
    assert getCost(4.0, 0.30) == 1.20


def test_attention_decision():
    assert getAttention(4, 10) 


"""def test_invalid_unusual_input():     # This check is occuring inside the loop
    assert getSeverity(1, -0.05) == "Invalid powerDraw" """

def test_smart_feedback_high():
    feedback = getFeedback(2,0.7)
    assert "HIGH" in feedback

def test_smart_feedback_critical():
    feedback = getFeedback(5, 15)
    assert "CRITICAL" in feedback
