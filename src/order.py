# src/order.py

def calculate_total(items: list[dict]) -> float:
    if not items:
        return 0.0

    total = 0.0
    for item in items:
        if item["quantity"] < 0:
            raise ValueError("Количество товара не может быть отрицательным")
        total += item["price"] * item["quantity"]

    return round(total, 2)