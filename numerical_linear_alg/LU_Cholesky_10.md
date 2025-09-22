# LU and Cholesky decompositions

Let A be an invertible matrix. Our goal is to compute x in :
$$\begin{align}
Ax=b
\end{align}$$
If A has a bad condition number then this is bad.

The standard way is to do gaussian elimination.

Take row operations. take a matrix
$$\begin{align}
A= % 1 x 3 BMatrix
\begin{bmatrix}
a_1 & \dots & a_n
\end{bmatrix}
\end{align}$$
So to do gaussian elimination. we replace row one with row one. we replace $r_2=r_2-\frac{a_{2,1}}{a_{1,1}}r_1$. After all of this eliminatino we get:
$$\begin{align}
\begin{bmatrix}
a_{11} & \dots & \star \\
\vdots & \ddots & \vdots \\
0 & \dots & \star
\end{bmatrix}
\end{align}$$
As long as we do not divide by zero we are fine. because $r_{j}=r_j-\frac{a_{j1}}{a_{11}}r_1$
