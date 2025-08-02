import pytest

from template_cli_python.common import arithmetic_ops


def test_add() -> None:
    """Test add function"""
    assert arithmetic_ops.add(1, 1) == 2
    assert arithmetic_ops.add(2, 3) == 5


def test_sub() -> None:
    """Test sub function"""
    assert arithmetic_ops.sub(1, 1) == 0
    assert arithmetic_ops.sub(2, 3) == -1


def test_mul() -> None:
    """Test mul function"""
    assert arithmetic_ops.mul(1, 1) == 1
    assert arithmetic_ops.mul(2, 3) == 6


def test_div() -> None:
    """Test div function"""
    assert arithmetic_ops.div(1, 1) == 1
    assert arithmetic_ops.div(2, 3) == 0


def test_div_by_zero() -> None:
    """Test div function with zero divisor"""
    with pytest.raises(ZeroDivisionError) as e:
        arithmetic_ops.div(1, 0)

    assert str(e.value) == "Division by zero is not allowed."


def test_div_zero_numerator() -> None:
    """Test div function with zero numerator"""
    assert arithmetic_ops.div(0, 1) == 0
    assert arithmetic_ops.div(0, 3) == 0
