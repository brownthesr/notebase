# Diagonalizability

A matrix is diagonalizable if its similar to a diagonal matrix, iff its not defective.

Every matrix is bidiagonalizable (via jordan normal form)

This similarly matrix can be pretty awful with terrible norm. We would like nicer things.

## Unitary Diagonalization

Every matrix is unitarily similar to a upper triangular matrix. (Possibly one of the most useful decompositions that exists)

By the schur decomposition obviously hermitian matrices satisfy this by the schur lemma

If a matrix is unitarily diagonalizble with real eiganvalues it is hermitian and vice versa. Somehow this process of rearranging numbers reveals something about the spectrum of the matrix

first we show that the spectrum is real:
$$\begin{align}
(\lambda, v):\\
\langle v,Av\rangle=\lambda=\overline \lambda
\end{align}$$
Thus $\lambda$ is real

To prove that we have a orthonormal set of eigenvectors, we show that the space perpendicular to any eigenvector is invariant.

proof: Let $\lambda_1,v_1$ be an eigenpair of $A$, let $Q_1$ is unitary $[v_1,q_2,q_3,\dots,q_n]$

$$\begin{align}
Q_1^*AQ_1 \text{ is hermitian}\\
Q_1^*AQ_1=Q_1[Av_1, Aq_2,\dots Aq_n]\\
=Q_1^\star[\lambda_1v_1, Aq_2,\dots,Aq_n]\\
=% 4 x 4 BMatrix
\begin{bmatrix}
\lambda_1v_1^*v_1 & q_2^*A^*v_1 & \dots & q_n^*A^*v_1 \\
\lambda_1v_1^*q_2 & \vdots & \dots & \vdots \\
\vdots & \vdots & \ddots & \vdots \\
\dots & \dots & \dots & \dots
\end{bmatrix}\\
=% 4 x 4 BMatrix
\begin{bmatrix}
\lambda_1 & 0 & 0 & 0 \\
0 & * & * & * \\
0 & * & * & * \\
0 & * & * & *
\end{bmatrix}
\end{align}$$
### Geometric interpretation of hermitian matrices:
$$\begin{align}
A=U\Lambda U\\
=\sum\lambda_i u_iu_i^*
\end{align}$$
So it is just a sum of rank one matrices.

Recall $u_ju_j^*x$ is the projection of x onto $u_j$. Essentially we decompose any $x$ into the unitary directions, Stretch those however much we need to, then recombine. It is essentially a diagonal matrix in disguise.

## Induced 2 norm
$\rho(A)=\max_{j=1,\dots,n}|\lambda_j(A)|$ if A is hermitian then:
$$\begin{align}
||A||_2=\rho(A)
\end{align}$$
proof:
$$\begin{align}
||Ax||=||\sum u_j \lambda_j c_j||_2\\
=(\sum |c_j\lambda_j|^2)^\frac{1}{2}\leq \rho(A)\norm{c_j}=\rho(A)
\end{align}$$
This is achievable by choosing $x$ as an eigenvector of the largest eigenvalue.

$$\begin{align}
A=% 2 x 2 BMatrix
\begin{bmatrix}
0 & 10^10 \\
0 & 0
\end{bmatrix}
\end{align}$$
Even if they are diagonalizable we could have nasty things like this. Most of the time the norm of the matrix is not the spectral radius. The spectral radius is obviously a lower bound for the norm.

## A norm
### Definition
A matrix is hermitian positive definite sometimes called SPD. If its hermitian and its spectrum is strictly positive. Its typical to order the spectrum of spd matrices.

We can define the norm:
$$\begin{align}
||x||^2_A=x^*Ax
\end{align}$$
This is a norm iff $A$ is SPD.

## Square root of a matrix
A matrix B is the square root of a matrix $A$ if $A=B^2$. For example if A is SPD it has a square root
$$\begin{align}
A = U\Lambda U^*\\
B = U\sqrt{\Lambda}U^*
\end{align}$$
so $\sqrt{A}= B$

The goal is to create a functional calculus on SPD matrix.

## Quadratic Forms:
We can define a quadratic form:
$$\begin{align}
Q_A(x)=x^\star Ax
\end{align}$$
The eigendecomposition uniquely defines the behavior of $Q_A$ (We make sure this is hermitian by definition).

$$\begin{align}
Q_A(x)=(U^*x)^*\Lambda (U^*x)\\
y=U^*x\\
y^*\Lambda y = \lambda_1 |y_1|^2+\dots+\lambda_n|y_n|^2
\end{align}$$
This is a very transparent function. The eigenvalues tell us everything that is happening (quadratic bowls). So the bowl curves up in positive eigenvector directions, down in negative eigenvector directions, and flat on zero eigenvector directions.

## Raleigh quotient
$$\begin{align}
R_A(x):=\frac{Q_A(x)}{||x||_2^2}
\end{align}$$
Only if $x\neq 0$. We can do this for any square matrix. Obviously eigenvectors turn into eigenvalues.

It is also invariant under scaling.
## Numerical Range:
$$\begin{align}
W(A)=R_A(C^n\{0\})
\end{align}$$
Clearly the spectrum is inside this range. This is also bounded by the norm of the matrix. Its important that this is complex space.

Note that if A is hermitian then the numerical range is literally just a thing on the real line. Suppose that $||x||=1$ then $R_A(x)=x^*Ax=x^*U^*\Lambda Ux$ define $c=Ux$ then $R_A(x)=c^*\Lambda c=\sum \lambda_j |c_j|^2$ so this is always a real number. Order that $\lambda_1<\lambda_2<\dots\leq \lambda_n$ then that means that the raleigh quotient is a convex combination of things. so they are always greater than the smallest and larger than the greatest:
$$\begin{align}
\lambda_1\leq R_A(x)\leq \lambda_n
\end{align}$$
And these are achievable numbers in that these inequalities are sharp.

Now we will consider the image of the raleigh quotient of a subspace $V\subset C^n$

The minimum value of $R_A(V)$ is $\lambda_{min}$ this occurs when V contains the minimum eigenvector. What is the largest possible minimum value, or the smallest possible maximum value

## Courant-fischer-weyl min max theorem:
$$\begin{align}
\lambda_k = \min_{\substack{V\subset C^n\\ \dim V=k}}\max R_A(v)\\
\lambda_k = \max_{\substack{V\subset C^n\\ \dim V=k}}\min R_A(v)\\
\end{align}$$
The idea behind proof this: $k=n-1$

Let $V$ be any $(n-1)$ dimensional subspace. Let $u_j$ be the eigenvector of $A$ corresponding to $\lambda_j$

Define $W=\span\{u_{n-1},u_n\}$ so $\dim W=2$. this with the fact that $\dim V=n-1$ means that the intersection of the two is nonempty so

There must be $||v||=1$
$$\begin{align}
v\in V, v=c_{n-1}u_{n-1}+c_nu_{n}\\
R_A(v)=|c_{n-1}|^2\lambda_{n-1}+|c_n|^2\lambda_n\geq \lambda_{n-1}
\end{align}$$
We can achieve equality if we choose $V$ to contain $u_{n-1}$

So whatever subspace I choose
## Cauchy Interlacing theorem
Take some $Q\in C^{n\times r}$ with orthonormal collumns. $B=Q^*AQ$. So B is a compression of the matrix A.

If $B\in C^{(n-1)\times (n-1)}$ is a compression of a hermitian matrix then the eigenvalue interlace in that :
$$\begin{align}
\lambda_j\leq \mu_j\leq \lambda_{j+1}
\end{align}$$
