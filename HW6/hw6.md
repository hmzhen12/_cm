# 2D Geometric Transformations via Linear Algebra

This document explains the mathematical foundations of 2D geometric transformations using Linear Algebra. By utilizing **Homogeneous Coordinates**, we can represent Translation, Scaling, and Rotation as unified $3 \times 3$ matrices.

## 1. The Coordinate System

In standard Euclidean geometry, a point is $(x, y)$. In Linear Algebra for computer graphics, we represent this point as a **column vector**.

To enable **Translation** (which is an affine transformation, not a linear one in 2D space), we use **Homogeneous Coordinates** by adding a third component, usually $1$.

$$
\mathbf{v} = \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
$$

The general transformation equation is:
$$
\mathbf{v'} = M \cdot \mathbf{v}
$$

---

## 2. Transformation Matrices

### A. Translation (Moving)
To move a point by a distance $d_x$ along the X-axis and $d_y$ along the Y-axis.

* **Logic:** $x' = x + d_x$, $y' = y + d_y$
* **Matrix:**

$$
T(d_x, d_y) = \begin{bmatrix} 
1 & 0 & d_x \\ 
0 & 1 & d_y \\ 
0 & 0 & 1 
\end{bmatrix}
$$

### B. Scaling (Resizing)
To stretch or shrink an object by a factor of $s_x$ (width) and $s_y$ (height).

* **Logic:** $x' = x \cdot s_x$, $y' = y \cdot s_y$
* **Matrix:**

$$
S(s_x, s_y) = \begin{bmatrix} 
s_x & 0 & 0 \\ 
0 & s_y & 0 \\ 
0 & 0 & 1 
\end{bmatrix}
$$

### C. Rotation (Spinning)
To rotate a point counter-clockwise by an angle $\theta$ around the origin $(0,0)$.

* **Logic:** Uses trigonometric identities to map the new coordinates.
* **Matrix:**

$$
R(\theta) = \begin{bmatrix} 
\cos\theta & -\sin\theta & 0 \\ 
\sin\theta & \cos\theta & 0 \\ 
0 & 0 & 1 
\end{bmatrix}
$$

---

## 3. Matrix Composition (Combining Transformations)

To apply multiple transformations, you multiply the matrices together. Because matrix multiplication is **not commutative** ($A \cdot B \neq B \cdot A$), the order is critical.

Since we use column vectors, transformations are applied from **Right to Left**.

**Example:**
To **Rotate** first ($R$), and then **Translate** ($T$):

$$
\mathbf{v'} = T \cdot (R \cdot \mathbf{v}) = (T \cdot R) \cdot \mathbf{v}
$$

1.  Calculate the combined matrix $M = T \cdot R$.
2.  Apply $M$ to the vector $\mathbf{v}$.

---

## 4. Summary Table

| Transformation | Matrix Representation | Variables |
| :--- | :--- | :--- |
| **Translation** | $\begin{bmatrix} 1 & 0 & d_x \\ 0 & 1 & d_y \\ 0 & 0 & 1 \end{bmatrix}$ | $d_x, d_y$: Distance to move |
| **Scaling** | $\begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | $s_x, s_y$: Scale factor ($1 =$ no change) |
| **Rotation** | $\begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | $\theta$: Angle in radians/degrees |
| **Identity** | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | No change |
