def strategy(age, amount):
    if age < 40:
        return 0, 0.2*amount, 0.8*amount
    if age >= 40 and age < 60:
        return 0, 0.5*amount, 0.5*amount
    if age >= 60:
        return 0.333*amount, 0.333*amount, 0.334*amount
