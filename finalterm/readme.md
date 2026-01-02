# 程式與數學 期末作業
## 111210548 資工三 胡眉真
### 習題 1: 請用程式驗證微積分基本定理

[Homework 1](https://github.com/hmzhen12/_cm/tree/main/HW1)

使用[Chatgpt](https://chatgpt.com/share/6907222d-b538-800c-bf0c-b081779c73ca)協助debug

### 習題 2:  請寫程式求解二次多項式的根

[Homework 2](https://github.com/hmzhen12/_cm/tree/main/HW2)
使用[Chatgpt](https://chatgpt.com/share/690720b5-62d8-800c-9de2-bce2935d4534)協助debug

### 習題 3 : 請寫程式求解三次多項式的根 (加分題）

[Homework 3](https://github.com/hmzhen12/_cm/tree/main/HW3)
使用[Chatgpt](https://chatgpt.com/share/69072589-6264-800c-9dd5-bc6c9a7efb5c)協助debug

### 習題4： （思考）請寫一個函數 root(c) 求出 n 次多項式的根 （ n>=5 的時候，數學上證明沒有公式 -- 伽羅瓦定理）

[Homework 4](https://github.com/hmzhen12/_cm/tree/main/HW4)
使用[Chatgpt](https://chatgpt.com/share/69072941-f6fc-800c-9a8d-d189eeb783d1)協助debug

### 習題5: 有限體

[Homework 5](https://github.com/hmzhen12/_cm/tree/main/HW5)
使用[Chatgpt](https://chatgpt.com/share/69157786-90d8-800c-ae9c-106f40d3b1fe)

### 習題6: 幾何學：（點，線，圓）世界的建構 

[Homework 6](https://github.com/hmzhen12/_cm/tree/main/HW6)
使用[Google Gemini](https://gemini.google.com/share/9396039db10a)協助debug

### 習題7: 機率統計 - 檢定背後的數學原理

[Homework 7](https://gemini.google.com/share/7088a27c6312)
使用Google Gemini問答，理解 z 檢定與 t 檢定背後的數學原理 (包含公式是如何推導出來的）

### 習題8: 資訊理論

[Homework 8](https://github.com/hmzhen12/_cm/tree/main/HW8)
使用[Chatgpt](https://chatgpt.com/share/69579384-d95c-800c-a1b9-ad8312a83bc0)

### 習題9: 線性代數

[Homework 9](https://github.com/hmzhen12/_cm/tree/main/HW9)
使用[Chatgpt](https://chatgpt.com/share/69579546-23f4-800c-ad4d-2811e4e69a87)

### 習題10: 請寫出傅立葉正轉換和逆轉換的函數（不要用套件）

[Homework 10](https://github.com/hmzhen12/_cm/tree/main/HW10)
使用[Chatgpt](https://chatgpt.com/share/69579dd7-f410-8006-96e9-9f5f4ffe18d8)

### 習題11: 請寫程式求解常係數齊次常微分方程

[Homework 11](https://github.com/hmzhen12/_cm/tree/main/HW11)
使用[Chatgpt](https://chatgpt.com/share/6957a4e5-da98-8006-b33c-7fc727836a41)

### 期中作業

[Midterm](https://github.com/hmzhen12/_cm/tree/main/midterm)
使用[Chatgpt](https://chatgpt.com/share/69072941-f6fc-800c-9a8d-d189eeb783d1)
# Prime Number Analysis & Simple Cryptography
I used AI to help me to do this project. So, this is the reference form ChatGPT: https://chatgpt.com/share/6956aaa3-8d0c-800c-bb0c-fa9f8b476ae9

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

---

## References
1. Rivest, R., Shamir, A., & Adleman, L. (1978). A Method for Obtaining Digital Signatures and Public-Key Cryptosystems. Communications of the ACM, 21(2), 120–126.
2. Crandall, R., & Pomerance, C. (2005). Prime Numbers: A Computational Perspective. Springer.
3. Menezes, A., van Oorschot, P., & Vanstone, S. (1996). Handbook of Applied Cryptography. CRC Press.
4. Python math module documentation: (https://docs.python.org/3/library/math.html)
5. Miller-Rabin primality test: (https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) 


