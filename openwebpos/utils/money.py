def convert_to_cents(amount: float):
    """
    Convert the amount to cent.

    Args:
        amount: Amount.

    Returns:
        int: Amount in cent.
    """
    return int(amount * 100)


def convert_to_dollar(amount: int):
    """
    Convert the amount to dollar.

    Args:
        amount: Amount.

    Returns:
        float: Amount in dollar.
    """
    return float(amount / 100)
