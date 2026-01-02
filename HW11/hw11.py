import numpy as np
from collections import defaultdict

def solve_ode_general(coefficients, tol=1e-6):
    """
    Solve homogeneous linear ODE with constant coefficients.
    """

    roots = np.roots(coefficients)

    # ---- Step 1: Cluster roots numerically ----
    clusters = []
    for r in roots:
        for cluster in clusters:
            if abs(r - cluster[0]) < tol:
                cluster.append(r)
                break
        else:
            clusters.append([r])

    solution = []
    C = 1

    # ---- Step 2: Build solution from clusters ----
    for cluster in clusters:
        root = cluster[0]
        m = len(cluster)

        alpha = root.real
        beta = root.imag

        # ---- Real root ----
        if abs(beta) < tol:
            for k in range(m):
                if k == 0:
                    solution.append(f"C_{C} e^({alpha:.3g}x)")
                else:
                    solution.append(f"C_{C} x^{k} e^({alpha:.3g}x)")
                C += 1

        # ---- Complex conjugate pair ----
        elif beta > 0:
            beta = abs(beta)
            for k in range(m):
                if k == 0:
                    solution.append(f"C_{C} e^({alpha:.3g}x) cos({beta:.3g}x)")
                    C += 1
                    solution.append(f"C_{C} e^({alpha:.3g}x) sin({beta:.3g}x)")
                    C += 1
                else:
                    solution.append(f"C_{C} x^{k} e^({alpha:.3g}x) cos({beta:.3g}x)")
                    C += 1
                    solution.append(f"C_{C} x^{k} e^({alpha:.3g}x) sin({beta:.3g}x)")
                    C += 1

    return "y(x) = " + " + ".join(solution)
