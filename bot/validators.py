def validate_side(side):
    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Invalid side. Allowed values: BUY, SELL")

    return side


def validate_order_type(order_type):
    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError(
            "Invalid order type. Allowed values: MARKET, LIMIT, STOP_LIMIT"
        )

    return order_type

def validate_positive_number(value, field_name):
    if value is None:
        raise ValueError(
            f"{field_name} is required"
        )

    if value <= 0:
        raise ValueError(
            f"{field_name} must be greater than 0"
        )

    return value