# Prime Number Analysis & Simple Cryptography

## Project Description
This project performs **prime number analysis**, **probabilistic primality testing**, and demonstrates a **basic RSA cryptosystem**.  

The program can:
- Check if a number is prime using the **Miller-Rabin probabilistic test**.
- Compute **GCD (Greatest Common Divisor)** and **LCM (Least Common Multiple)** of two numbers.
- Generate a **simple RSA key pair** (public & private keys) for educational purposes.

This project is suitable for learning **number theory**, **cryptography basics**, and implementing **mathematical algorithms in Python**.

---

## Mathematical Foundation
1. **Prime Numbers**  
   A prime number is a positive integer greater than 1 with no positive divisors other than 1 and itself.

2. **Miller-Rabin Primality Test**  
   A probabilistic algorithm for testing whether a number is prime.  
   For a given number \(n\), write \(n-1 = 2^r \cdot d\) with \(d\) odd.  
   Randomly choose bases \(a\) and check if \(a^d \equiv 1 \pmod{n}\) or \(a^{2^j d} \equiv -1 \pmod{n}\) for \(0 \le j < r\).  
   If these fail, \(n\) is composite; otherwise, \(n\) is likely prime.

3. **GCD & LCM**  
   - **GCD (Greatest Common Divisor)**: largest integer dividing two numbers.  
   - **LCM (Least Common Multiple)**: smallest integer divisible by both numbers.  
   Relationship:  
   \[
   LCM(a, b) = \frac{|a \cdot b|}{GCD(a, b)}
   \]

4. **RSA Cryptography (Simplified)**  
   - Based on two large primes \(p\) and \(q\).  
   - Compute \(n = p \cdot q\) and \(\phi(n) = (p-1)(q-1)\).  
   - Choose \(e\) such that \(\gcd(e, \phi(n)) = 1\).  
   - Compute \(d\) as modular inverse of \(e\) modulo \(\phi(n)\).  
   - Public key: \((e, n)\), Private key: \((d, n)\).  

---

## Implementation Details
- **Language**: Python 3  
- **Libraries**: `math`, `random`  
- **Algorithms Used**:
  - **Sieve of Eratosthenes** for generating small prime numbers.  
  - **Miller-Rabin Test** for probabilistic primality testing.  
  - **Euclidean Algorithm** for GCD.  
  - **LCM** computed using relationship with GCD.  
  - **RSA key generation**: select two random primes, compute n, φ(n), e, d.

- **Program Workflow**:
  1. Ask user for a number to check for primality.  
  2. Ask user for two numbers to compute GCD and LCM.  
  3. Generate a simple RSA key pair.  
  4. Print all results.

---

## How to Run
1. Install Python 3.x if not installed.
2. Save the code in a file named `prime_crypto_analysis.py`.
3. Open terminal/command prompt and navigate to the file directory.
4. Run the program:
   ```bash
   python prime_crypto_analysis.py
