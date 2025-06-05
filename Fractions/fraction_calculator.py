from fractions import Fraction

def add_fractions(frac1: str, frac2: str) -> str:
    f1 = Fraction(frac1)
    f2 = Fraction(frac2)
    result = f1 + f2

    whole = result.numerator // result.denominator
    remainder = result.numerator % result.denominator

    if whole != 0 and remainder != 0:
        return f"{whole} {Fraction(remainder, result.denominator)}"
    elif whole != 0:
        return f"{whole}"
    else:
        return f"{Fraction(remainder, result.denominator)}"

# Benutzer-Eingabe
frac1 = input("Gib den ersten Bruch ein (z.B. 1/2): ")
frac2 = input("Gib den zweiten Bruch ein (z.B. 3/4): ")

# Ergebnis anzeigen
print(f"{frac1} + {frac2} = {add_fractions(frac1, frac2)}")

# Von Benjamin Wilk
