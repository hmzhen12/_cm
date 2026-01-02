# Information Theory and Coding Demo

This project demonstrates key concepts in probability, information theory,
and error-correcting codes using Python.

---

## 1. Probability of All Heads

For a fair coin with probability p = 0.5, the probability of getting heads
10,000 times in a row is:

P = p^10000

This value is extremely close to zero and cannot be represented accurately
using standard floating-point arithmetic.

---

## 2. Logarithmic Probability

To avoid numerical underflow, we compute:

log(p^n) = n log(p)

For p = 0.5 and n = 10,000, this gives a finite and computable result.

---

## 3. Information Theory Metrics

### Entropy
Measures the uncertainty of a probability distribution.

H(p) = -Σ p(x) log₂ p(x)

### Cross Entropy
Measures how well distribution q approximates p.

H(p, q) = -Σ p(x) log₂ q(x)

### KL Divergence
Measures the difference between two distributions.

D_KL(p || q) = Σ p(x) log₂ (p(x) / q(x))

### Mutual Information
Measures shared information between two variables.

I(X;Y) = Σ p(x,y) log₂ [ p(x,y) / (p(x)p(y)) ]

---

## 4. Cross Entropy Inequality

The program verifies that:

H(p, p) < H(p, q) when q ≠ p

This reflects that cross entropy is minimized when q = p.

---

## 5. (7,4) Hamming Code

The (7,4) Hamming code encodes 4 data bits into 7 bits
by adding 3 parity bits. It can detect and correct a
single-bit error.

Functions included:
- Encoding
- Error detection
- Error correction
- Decoding

---

## 6. Shannon Channel Coding Theorem

The Shannon Channel Coding Theorem states that for a noisy
channel with capacity C, it is possible to transmit information
reliably at any rate R < C using appropriate coding.

---

## 7. Shannon–Hartley Theorem

The Shannon–Hartley Theorem defines the channel capacity of
a band-limited Gaussian channel:

C = B log₂(1 + S/N)

where:
- B is bandwidth
- S is signal power
- N is noise power

This theorem sets the theoretical upper bound on data transmission rates.
