import numpy as np

def dft_continuous(f, x_min, x_max, omega_vals, num_points=10000):
    """
    F(ω) = ∫ f(x) e^{-iωx} dx
    """
    x = np.linspace(x_min, x_max, num_points)
    dx = x[1] - x[0]
    fx = f(x).astype(complex)

    F = np.zeros(len(omega_vals), dtype=complex)
    for i, omega in enumerate(omega_vals):
        F[i] = np.sum(fx * np.exp(-1j * omega * x)) * dx

    return F


def idft_continuous(F_vals, omega_vals, x_vals):
    """
    f(x) = (1 / 2π) ∫ F(ω) e^{iωx} dω
    """
    domega = omega_vals[1] - omega_vals[0]
    f_rec = np.zeros(len(x_vals), dtype=complex)

    for i, x in enumerate(x_vals):
        f_rec[i] = np.sum(F_vals * np.exp(1j * omega_vals * x)) \
                   * domega / (2 * np.pi)

    return f_rec


if __name__ == "__main__":
    f = lambda x: np.exp(-x**2)

    x_min, x_max = -5, 5
    omega_vals = np.linspace(-10, 10, 2000)
    x_vals = np.linspace(x_min, x_max, 400)

    F_vals = dft_continuous(f, x_min, x_max, omega_vals)
    f_rec = idft_continuous(F_vals, omega_vals, x_vals)

    f_true = f(x_vals)
    error = np.max(np.abs(f_true - f_rec.real))

    print("Maximum reconstruction error:", error)
