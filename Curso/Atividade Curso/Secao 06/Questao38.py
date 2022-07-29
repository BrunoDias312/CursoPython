"""
Fazer com que A² + B² seja igual a 1000
"""

valor = 0

while valor <= 1000:
    for a in range(1000):
        for b in range(1000):
            c = a ** 2 + b ** 2
            if c == 1000:
                print(f"{a}² + {b}² = {c}")
    break
