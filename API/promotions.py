# promotions.py
def get_spend_type(cluster):
    # Spend type is the second item in the list (index 1)
    return cluster[1]

def get_promotion(spend_type):
    promotions = {
        "bills": "5% off on Utility Bills",
        "food": "Buy One Get One Free on Meals",
        "entertainment": "Free Movie Tickets with Purchase",
        "grocery": "10% off on Groceries",
        "fuel": "10% off on Fuel",
        "travel": "Free Travel Insurance"
    }
    return promotions.get(spend_type.lower(), "No promotion available")

# Example usage
spend_type = "fuel"
print(get_promotion(spend_type))  # Output: 10% off on Fuel

spend_type = "bills"
print(get_promotion(spend_type))  # Output: 5% off on Utility Bills
