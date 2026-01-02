import math
import numpy as np

# ==================================================
# 1. Probability of all heads
# ==================================================
def probability_all_heads(p=0.5, n=10000):
    """
    Direct computation (will underflow for large n).
    """
    return p ** n


def log_probability(p=0.5, n=10000):
    """
    Numerically stable computation using logs.
    """
    return n * math.log(p)


# ==================================================
# 2. Information Theory Functions
# ==================================================
def entropy(p):
    if not math.isclose(sum(p), 1.0):
        raise ValueError("Probability distribution must sum to 1.")
    return -sum(pi * math.log2(pi) for pi in p if pi > 0)


def cross_entropy(p, q):
    if not math.isclose(sum(p), 1.0) or not math.isclose(sum(q), 1.0):
        raise ValueError("Distributions must sum to 1.")
    if any(qi == 0 and pi > 0 for pi, qi in zip(p, q)):
        raise ValueError("q contains zero where p is non-zero.")
    return -sum(pi * math.log2(qi) for pi, qi in zip(p, q) if pi > 0)


def kl_divergence(p, q):
    if not math.isclose(sum(p), 1.0) or not math.isclose(sum(q), 1.0):
        raise ValueError("Distributions must sum to 1.")
    if any(qi == 0 and pi > 0 for pi, qi in zip(p, q)):
        raise ValueError("q contains zero where p is non-zero.")
    return sum(pi * math.log2(pi / qi) for pi, qi in zip(p, q) if pi > 0)


def mutual_information(joint):
    joint = np.array(joint, dtype=float)
    if not math.isclose(joint.sum(), 1.0):
        raise ValueError("Joint distribution must sum to 1.")

    px = joint.sum(axis=1)
    py = joint.sum(axis=0)

    mi = 0.0
    for i in range(joint.shape[0]):
        for j in range(joint.shape[1]):
            if joint[i, j] > 0:
                mi += joint[i, j] * math.log2(
                    joint[i, j] / (px[i] * py[j])
                )
    return mi


# ==================================================
# 3. Cross Entropy Inequality Verification
# ==================================================
def verify_cross_entropy():
    p = [0.5, 0.5]
    q = [0.9, 0.1]

    h_pp = cross_entropy(p, p)
    h_pq = cross_entropy(p, q)

    # Correct inequality: H(p,p) <= H(p,q)
    return h_pp, h_pq, h_pp <= h_pq


# ==================================================
# 4. (7,4) Hamming Code
# ==================================================
def hamming_encode(data):
    """
    Encode 4 bits into 7-bit Hamming code.
    Bit positions: [p1, p2, d1, p3, d2, d3, d4]
    """
    d1, d2, d3, d4 = data
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4
    return [p1, p2, d1, p3, d2, d3, d4]


def hamming_decode(code):
    """
    Decode and correct one-bit error.
    """
    c = code.copy()
    p1, p2, d1, p3, d2, d3, d4 = c

    s1 = p1 ^ d1 ^ d2 ^ d4
    s2 = p2 ^ d1 ^ d3 ^ d4
    s3 = p3 ^ d2 ^ d3 ^ d4

    error_position = s1 + (s2 << 1) + (s3 << 2)

    if error_position != 0:
        c[error_position - 1] ^= 1  # correct error

    _, _, d1, _, d2, d3, d4 = c
    return [d1, d2, d3, d4]


# ==================================================
# 5. Main Test
# ==================================================
if __name__ == "__main__":
    print("P(all heads):", probability_all_heads())
    print("log(P):", log_probability())

    p = [0.5, 0.5]
    q = [0.9, 0.1]

    print("Entropy:", entropy(p))
    print("Cross Entropy:", cross_entropy(p, q))
    print("KL Divergence:", kl_divergence(p, q))

    joint = [[0.25, 0.25], [0.25, 0.25]]
    print("Mutual Information:", mutual_information(joint))

    h_pp, h_pq, valid = verify_cross_entropy()
    print("H(p,p):", h_pp)
    print("H(p,q):", h_pq)
    print("H(p,p) <= H(p,q):", valid)

    data = [1, 0, 1, 1]
    encoded = hamming_encode(data)
    encoded[2] ^= 1  # inject 1-bit error
    decoded = hamming_decode(encoded)

    print("Original:", data)
    print("Decoded :", decoded)
