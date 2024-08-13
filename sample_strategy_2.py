def strategy(age, amount):
    if amount < 500000:
        return 0, 0, amount
    if amount >= 500000 and amount < 750000:
        return 0, 0.2*amount, 0.8*amount
    if amount >= 750000 and amount < 1000000:
        return 0.1*amount, 0.3*amount, 0.6*amount
    if amount >= 1000000:
        return amount, 0, 0
