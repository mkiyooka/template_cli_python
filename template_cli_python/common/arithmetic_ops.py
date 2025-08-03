"""
四則演算

四則演算関数により型ヒントの記述方法と、docstringの書き方を説明
"""


def add(lhs: float, rhs: float) -> float:
    """Addition function

    Performs addition.

    Parameters
    ----------
    lhs: float
        Left hand side
    rhs: float
        Right hand side

    Returns
    -------
        (float): Sum of lhs and rhs

    Examples
    --------
    >>> add(2, 3)
    5
    """
    return lhs + rhs


def sub(lhs: float, rhs: float) -> float:
    """Subtraction function

    Performs subtraction.

    Parameters
    ----------
    lhs: float
        Left hand side
    rhs: float
        Right hand side

    Returns
    -------
    (float): Difference obtained by subtracting rhs from lhs

    Examples
    --------
    >>> sub(2, 3)
    -1
    """
    return lhs - rhs


def mul(lhs: float, rhs: float) -> float:
    """Multiplication function

    Performs multiplication.

    Parameters
    ----------
    lhs: float
        Left hand side
    rhs: float
        Right hand side

    Returns
    -------
    num: lhs * rhs

    Examples
    --------
    >>> mul(2, 3)
    6
    """
    return lhs * rhs


def div(lhs: float, rhs: float) -> float:
    """Division function

    Performs division.

    Parameters
    ----------
    lhs: float
        Left hand side
    rhs: float
        Right hand side

    Returns
    -------
    quotient: float
    The quotient obtained by integer division of lhs by rhs.

    Examples
    --------
    >>> div(2, 3)
    0
    """
    if rhs == 0:
        msg = "Division by zero is not allowed."
        raise ZeroDivisionError(msg)
    if lhs == 0:
        return 0

    return lhs // rhs
