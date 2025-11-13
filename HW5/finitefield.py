class GF:
    def __init__(self, p, value):
        if p <= 1:
            raise ValueError("p must be a prime > 1")
        self.p = p
        self.value = value % p  # always keep inside [0, p-1]

    def __add__(self, other):
        self._check_same_field(other)
        return GF(self.p, (self.value + other.value) % self.p)

    def __sub__(self, other):
        self._check_same_field(other)
        return GF(self.p, (self.value - other.value) % self.p)

    def __mul__(self, other):
        self._check_same_field(other)
        return GF(self.p, (self.value * other.value) % self.p)

    def __truediv__(self, other):
        self._check_same_field(other)
        if other.value == 0:
            raise ZeroDivisionError("cannot divide by zero in a field")
        # Modular inverse (works in Python 3.8+)
        inv = pow(other.value, -1, self.p)
        return GF(self.p, (self.value * inv) % self.p)

    def __eq__(self, other):
        return isinstance(other, GF) and self.p == other.p and self.value == other.value

    def __repr__(self):
        return f"GF({self.p}, {self.value})"

    def _check_same_field(self, other):
        if not isinstance(other, GF) or self.p != other.p:
            raise ValueError("Elements must be from the same finite field")


# ===== Group and field checks =====

def check_distributivity(p):
    for a in range(p):
        for b in range(p):
            for c in range(p):
                A, B, C = GF(p, a), GF(p, b), GF(p, c)
                if not (A * (B + C) == (A * B) + (A * C)):
                    print(f"Fails distributivity: a={a}, b={b}, c={c}")
                    return False
    return True


def check_addition_group(p):
    elements = [GF(p, x) for x in range(p)]
    zero = GF(p, 0)

    # Closure
    for a in elements:
        for b in elements:
            if (a + b) not in elements:
                print(f"Fails closure at a={a}, b={b}")
                return False

    # Associativity
    for a in elements:
        for b in elements:
            for c in elements:
                if (a + (b + c)) != ((a + b) + c):
                    print(f"Fails associativity at a={a}, b={b}, c={c}")
                    return False

    # Commutativity
    for a in elements:
        for b in elements:
            if a + b != b + a:
                print(f"Fails commutativity at a={a}, b={b}")
                return False

    # Identity
    for a in elements:
        if not (a + zero == a and zero + a == a):
            print(f"Fails identity at a={a}")
            return False

    # Inverses
    for a in elements:
        if not any(a + b == zero for b in elements):
            print(f"Fails inverse at a={a}")
            return False

    return True


def check_multiplication_group(p):
    elements = [GF(p, x) for x in range(1, p)]  # exclude 0
    one = GF(p, 1)

    # Closure
    for a in elements:
        for b in elements:
            prod = a * b
            if prod.value == 0 or prod not in elements:
                print(f"Fails closure at a={a}, b={b}")
                return False

    # Associativity
    for a in elements:
        for b in elements:
            for c in elements:
                if (a * (b * c)) != ((a * b) * c):
                    print(f"Fails associativity at a={a}, b={b}, c={c}")
                    return False

    # Commutativity
    for a in elements:
        for b in elements:
            if a * b != b * a:
                print(f"Fails commutativity at a={a}, b={b}")
                return False

    # Identity
    for a in elements:
        if not (a * one == a and one * a == a):
            print(f"Fails identity at a={a}")
            return False

    # Inverses
    for a in elements:
        if not any(a * b == one for b in elements):
            print(f"Fails inverse at a={a}")
            return False

    return True


# ===== Main Test =====
if __name__ == "__main__":
    a = GF(5, 2)
    b = GF(5, 3)
    print("a =", a)
    print("b =", b)
    print("a + b =", a + b)
    print("a * b =", a * b)
    print("b - a =", b - a)
    print("b / a =", b / a)

    print("\n--- Field Property Checks for GF(5) ---")
    print("Distributivity:", check_distributivity(5))
    print("Addition forms a group:", check_addition_group(5))
    print("Multiplication (without 0) forms a group:", check_multiplication_group(5))
