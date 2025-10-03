# LU and Cholesky decompositions

Let A be an invertible matrix. Our goal is to compute x in :
$$\begin{align}
Ax=b
\end{align}$$
If A has a bad condition number then this is bad.

The standard way is to do gaussian elimination.

Take row operations. Take a matrix
$$\begin{align}
A= % 1 x 3 BMatrix
\begin{bmatrix}
a_1 & \dots & a_n
\end{bmatrix}
\end{align}$$
So to do gaussian elimination. We replace row one with row one. We replace $r_2=r_2-\frac{a_{2,1}}{a_{1,1}}r_1$. After all of this elimination we get:
$$\begin{align}
\begin{bmatrix}
a_{11} & \dots & \star \\
\vdots & \ddots & \vdots \\
0 & \dots & \star
\end{bmatrix}
\end{align}$$
As long as we do not divide by zero we are fine. Because $\tilde{r_{j}^*}=r_j^*-\frac{a_{j1}}{a_{11}}\tilde r_1^\star$. The idea here is that each row operation can be represented as a elementary matrix.

Rearranging for the original row:
$$\begin{align}
r_j^*=\tilde{r_j^*}+\frac{a_{j1}}{a_{11}}\tilde r_1^*\\
A=L_1A_2\\
L_1=% 2 x 2 BMatrix
\begin{bmatrix}
l & 0 \\
l & I
\end{bmatrix}\\
A_2=% 2 x 2 BMatrix
\begin{bmatrix}
a_{11} & \star \\
0 & \star
\end{bmatrix}
\end{align}$$
Where $l=% 4 x 1 BMatrix
\begin{bmatrix}
1 \\
\frac{a_{21}}{a_{11}}  \\
\vdots \\
\frac{a_{n1}}{a_{11}}
\end{bmatrix}$
note that $L_1$ is invertible because the diagonals are 1. This means that if $A$ is full rank then so is $A_2$

$$\begin{align}
L_j=% 1 x 4 BMatrix
\begin{bmatrix}
e_1 & \dots & l_j & \dots & e_n
\end{bmatrix}\\
A=L_1L_2\dots L_{n-1}A_n
\end{align}$$
furthermore note that $l_{j}$ is zero in the first j entries and a $1$ in the $j+1$ entry. So only the last rows suffer elimination. $A_n$ is upper diagonal. Then note that the product of lower triangular matrices is lower triangular so $L=L_1\dots L_{n-1}$ is lower triangular and we have the LU decomposition $A=LU$. Note L you can just move all of the L columns together.

This step can only fail if one of the pivots is zero. As long as the determinants of the principle sub-matrices are nonzero. The reason this is is because $det(A)=det(L)det(U)$ So A is invertible if and only if U is invertible.

Proof:

At step j of gaussian elimination consider $j\times j$ principle sub-matrix $A=L_1\dots L_jA_j$ where $A_j$ is almost upper triangular. The upper left j principle sub matrix is upper triangular. Call these upper matrices $A_j=L_jU_j$ where $L$ is invertible. Note that $(U_j)_{k,k}$ is not zero for $k<j$ because gaussian elimination was successful. But it is zero if $j=k$ iff A is not invertible. So we cannot do gaussian elimination if that is the case, but we can if A's sub-matrix is invertible.

## Talk about LU.

- This is how we solve linear systems
- Note that $\det(A)=\det(L)\det(U)=\det(U)$ So it is the product of the pivots. (This is exactly how people compute derivatives on computer)
- Solving $LU$ systems is really easy it only takes $O(n^2)$ (assuming you have $LU$ available).

$$\begin{align}
||x||_1=\sum_{i}|x_i|\leq n\max{x}=n||x||_\infty\\
||x||_\infty=\max |x_i|\leq \sum_{i}|x_i|\\
||x||_2^2=\sum |x_j|^2\leq n\max|x_j|^2=||x||_\infty^nn\\
||x||_\infty^2 = \max|x_j|^2\leq \sum |x_j|^2=||x||_2^2\\
||x||_2^2=\sum_i |x_i|^2\leq \sum_i|x_i|^2+\sum_{i\neq j}|x_i||x_j|=||x||_1^2\\
||x||_1=\sum_i|x_j|*1\leq ||x||_2\sqrt{n}\\
y=ABx,y=A(Bx)\\
(AB)_{ij}=\sum_{k}A_{ik}B_{kj}\\
fro(AB)^2=\sum_{ij}(\sum_{k}|A_{ik}B_{kj}|)^2\\
\leq \sum_{ij}||A_{i:}||^2||B_{:j}|^2\\
\end{align}$$

The idea is that we typically pivot with the max element in the column.

Note that row pivoting always works if A is invertible.

All of these pivoting strategies are typically $n^3$.

## Cholesky
Let A be hermitian positive definite.

$$\begin{align}
A= L_1B^*\\
=% 2 x 2 BMatrix
\begin{bmatrix}
1 & 0 \\
v/a & I
\end{bmatrix}% 2 x 2 BMatrix
\begin{bmatrix}
a & v^* \\
0 & A_2-vv^*/a
\end{bmatrix}\\
=\begin{bmatrix}
\sqrt{a} & 0 \\
v/\sqrt a & I
\end{bmatrix}% 2 x 2 BMatrix
\begin{bmatrix}
1 & 0 \\
0 & A_2-vv^*/a
\end{bmatrix}% 2 x 2 BMatrix
\begin{bmatrix}
\sqrt{a} & v^*/\sqrt a \\
0 & I
\end{bmatrix}
\end{align}$$
