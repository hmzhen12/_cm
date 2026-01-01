import random
import math

def sieve(n):
    """生成小於等於 n 的所有質數"""
    prime = [True] * (n + 1)
    prime[0:2] = [False, False]
    for p in range(2, int(n ** 0.5) + 1):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
    return [x for x, is_prime in enumerate(prime) if is_prime]


def is_prime_miller_rabin(n, k=5):
    """使用 Miller-Rabin 機率質數測試"""
    if n < 2:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # 將 n-1 表示為 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def generate_rsa_keys(bits=16):
    """生成簡單 RSA 公鑰與私鑰"""
    # 從小範圍隨機選擇兩個質數
    primes = [p for p in range(2 ** (bits-1), 2 ** bits) if is_prime_miller_rabin(p)]
    p = random.choice(primes)
    q = random.choice(primes)
    while q == p:
        q = random.choice(primes)
    
    n = p * q
    phi = (p-1)*(q-1)

    # 選擇 e 與 phi 互質
    e = 3
    while gcd(e, phi) != 1:
        e += 2

    # 計算 d (modular inverse)
    d = pow(e, -1, phi)
    return (e, n), (d, n)  # (公鑰, 私鑰)


def main():
    print("=== 質數分析與簡單 RSA ===")

    n = int(input("請輸入要檢查的質數："))
    print(f"{n} {'是質數' if is_prime_miller_rabin(n) else '不是質數'}")

    a = int(input("請輸入第一個數字計算 GCD/LCM："))
    b = int(input("請輸入第二個數字："))
    print(f"GCD({a}, {b}) = {gcd(a,b)}")
    print(f"LCM({a}, {b}) = {lcm(a,b)}")

    print("\n生成簡單 RSA 金鑰...")
    public, private = generate_rsa_keys()
    print(f"公鑰: {public}")
    print(f"私鑰: {private}")

if __name__ == "__main__":
    main()
