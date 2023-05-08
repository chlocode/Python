from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction, kpa_to_psi
from pytest import approx
import pytest

def test_water_column_height():
    """Tests the water_column_height function in water_flow.py
    Parameters: None
    Returns: nothing
    """
    assert water_column_height(0, 0) == 0
    assert water_column_height(0, 10) == approx(7.5)
    assert water_column_height(25, 0) == 25
    assert water_column_height(48.3, 12.8) == approx(57.9)


def test_pressure_gain_from_water_height():
    """Tests the pressure_gain_from_water_height function in water_flow.py
    Parameter(s): None
    Returns: nothing
    """
    assert pressure_gain_from_water_height(0, 9.80665, 998.2) == approx(0, abs = 0.001)
    assert pressure_gain_from_water_height(30.2, 9.80665, 998.2) == approx(295.628, abs = 0.001)
    assert pressure_gain_from_water_height(50, 9.80665, 998.2) == approx(489.450, abs = 0.001)

def test_pressure_loss_from_pipe():
    """Tests the pressure_loss_from_pipe function in water_flow.py
    Parameter(s): None
    Returns: nothing
    """
    assert pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75, 998.2) == approx(0, 0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0, 1.75, 998.2) == approx(0, abs = 0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 0, 998.2) == approx(0, abs =0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75, 998.2) == approx(-113.008, abs = 0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65, 998.2) == approx(-100.462, abs = 0.001)
    assert pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65, 998.2) == approx(-61.576, abs =0.001)
    assert pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65, 998.2) == approx(-110.884, abs =0.001)

def test_pressure_loss_from_fittings():
    """Tests the pressure_loss_from_pipe function in water_flow.py
    Parameter(s): None
    Returns: nothing
    """
    assert pressure_loss_from_fittings(0, 3, 998.2) == approx(0, abs = 0.001)
    assert pressure_loss_from_fittings(1.65, 0, 998.2) == approx(0, abs = 0.001)
    assert pressure_loss_from_fittings(1.65, 2, 998.2) == approx(-0.109, abs = 0.001)
    assert pressure_loss_from_fittings(1.75, 2, 998.2) == approx(-0.122, abs = 0.001)
    assert pressure_loss_from_fittings(1.75, 5, 998.2) == approx(-0.306, abs = 0.001)

def test_reynolds_number():
    """Tests the reynolds_number function in water_flow.py
    Parameter(s): None
    Returns: nothing
    """
    assert reynolds_number(0.048692, 0, 998.2) == approx(0, abs = 1)
    assert reynolds_number(0.048692, 1.65, 998.2) == approx(80069, abs = 1)
    assert reynolds_number(0.048692, 1.75, 998.2) == approx(84922, abs = 1)
    assert reynolds_number(0.28687, 1.65, 998.2) == approx(471729, abs = 1)
    assert reynolds_number(0.28687, 1.75, 998.2) == approx(500318, abs = 1)

def test_pressure_loss_from_pipe_reduction():
    """Tests the pressure_loss_from_pipe reduction in water_flow.py
    Parameter(s): None
    Returns: nothing
    """
    assert pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692, 998.2) == approx(0, abs = 0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692, 998.2) == approx(-163.744, abs = 0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692, 998.2) == approx(-184.182, abs = 0.001)

def test_kpa_to_psi():
    """Tests the kpa_to_psi function in water_flow.py
    Parameters: None
    Returns: nothing
    """
    assert kpa_to_psi(158.7) == approx(22.98, abs = 0.1)
    assert kpa_to_psi(0) == 0
    assert kpa_to_psi(-50) == approx(-7.2519, abs = 0.1)
    assert kpa_to_psi(123.45) == approx(17.8927, abs = 0.1)
    assert kpa_to_psi(-300) == approx(-43.5114, abs = 0.1)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])