def investment_advisor():
    market = input("Market up? (yes/no): ").lower()
    inflation = input("Inflation high? (yes/no): ").lower()
    risk = input("Risk (low/medium/high): ").lower()
    horizon = input("Horizon (short/long): ").lower()

    rules = {
        ('yes','no','high','long'): "STOCKS",
        ('yes','no','medium','long'): "MUTUAL FUNDS",
        ('no','yes','low','short'): "GOLD",
        ('no','yes','low','long'): "GOLD",
        ('yes','yes','medium','long'): "MUTUAL FUNDS",
        ('no','no','low','short'): "GOLD",
        ('yes','no','high','short'): "STOCKS"
    }

    result = rules.get(
        (market, inflation, risk, horizon),
        "MUTUAL FUNDS"
    )

    print("\nAnswer:", result)


if __name__ == "__main__":
    print("Where should I invest?\n")
    investment_advisor()