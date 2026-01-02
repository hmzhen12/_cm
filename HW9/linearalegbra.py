import numpy as np

# =========================================
# Recursive Determinant (Educational Only)
# =========================================
def det_recursive(A):
    A = np.asarray(A, dtype=float)
    n = A.shape[0]

    if n == 1:
        return A[0, 0]
    if n == 2:
        return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]

    det = 0.0
    for j in range(n):
        minor = np.delete(np.delete(A, 0, axis=0), j, axis=1)
        det += ((-1) ** j) * A[0, j] * det_recursive(minor)

    return det


# =========================================
# LU Decomposition (Doolittle Algorithm)
# =========================================
def lu_decomposition(A):
    A = np.asarray(A, dtype=float)
    n = A.shape[0]

    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        # Upper triangular
        for k in range(i, n):
            U[i, k] = A[i, k] - np.sum(L[i, :i] * U[:i, k])

        # Lower triangular
        L[i, i] = 1.0
        for k in range(i + 1, n):
            L[k, i] = (A[k, i] - np.sum(L[k, :i] * U[:i, i])) / U[i, i]

    return L, U


def det_lu(A):
    _, U = lu_decomposition(A)
    return np.prod(np.diag(U))


# =========================================
# Verify Matrix Decompositions
# =========================================
def verify_decompositions(A):
    print("\n--- Decomposition Verification ---")

    # LU
    L, U = lu_decomposition(A)
    print("LU reconstruction correct:",
          np.allclose(A, L @ U))

    # Eigen decomposition
    eigvals, eigvecs = np.linalg.eig(A)
    try:
        A_eig = eigvecs @ np.diag(eigvals) @ np.linalg.inv(eigvecs)
        print("Eigen reconstruction correct:",
              np.allclose(A, A_eig))
    except np.linalg.LinAlgError:
        print("Eigen reconstruction failed (non-invertible eigenvector matrix)")

    # SVD
    U_svd, S, Vt = np.linalg.svd(A)
    A_svd = U_svd @ np.diag(S) @ Vt
    print("SVD reconstruction correct:",
          np.allclose(A, A_svd))


# =========================================
# Eigen Decomposition → SVD (Symmetric Only)
# =========================================
def eigen_to_svd(A):
    A = np.asarray(A, dtype=float)

    # Must be symmetric
    if not np.allclose(A, A.T):
        raise ValueError("Matrix must be symmetric")

    eigvals, V = np.linalg.eigh(A)
    eigvals = np.maximum(eigvals, 0)

    S = np.sqrt(eigvals)
    eps = 1e-10

    U = A @ V @ np.diag(1 / (S + eps))
    return U, S, V.T


# =========================================
# PCA via SVD
# =========================================
def pca(X, k=2):
    X = np.asarray(X, dtype=float)
    X_centered = X - X.mean(axis=0)

    U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)
    return X_centered @ Vt[:k].T


# =========================================
# Main Execution
# =========================================
if __name__ == "__main__":
    np.random.seed(0)

    A = np.random.rand(3, 3)

    print("Matrix A:\n", A)
    print("\nRecursive determinant:", det_recursive(A))
    print("LU determinant:", det_lu(A))
    print("NumPy determinant:", np.linalg.det(A))

    verify_decompositions(A)

    # PCA test
    X = np.random.rand(100, 3)
    X_pca = pca(X, k=2)
    print("\nPCA output shape:", X_pca.shape)

    # Eigen → SVD test
    B = A.T @ A  # symmetric positive semi-definite
    U, S, Vt = eigen_to_svd(B)
    print("Eigen → SVD reconstruction correct:",
          np.allclose(B, U @ np.diag(S) @ Vt))
