# Matrix Exponentials

Last time we solved:
$$\begin{align}
\dot{x} = Ax\\
x(0)=x_0\\
x(t)=e^{At}x_0
\end{align}$$
we also talked about the non-homogenous situation
$$\begin{align}
x(t)=e^{At}x_0+ \int_0^te^{A(t-s)}f(s)ds
\end{align}$$
if $A$ is diagonal then we know we can just take the exponential component wise.

If A has n distinct eigenvalue then we can diagonalize it and get:
$$\begin{align}
e^{At} = Ve^{\Lambda t}V^{-1}
\end{align}$$

proof:
$$\begin{align}
e^{At} = \sum\limits_{k=0}^{\infty}\left(\frac{(At)^k}{k!}\right)\\
= \sum\limits_{k=0}^{\infty}\left(\frac{Q(\Lambda t)^kQ^{-1}}{k!}\right)\\
= Q\sum\limits_{k=0}^{\infty}\left(\frac{(\Lambda t)^k}{k!}\right)Q^{-1}\\
= Qe^{\Lambda t}Q^{-1}
\end{align}$$

## Dynamics of complex eigenvalues
If $A\in \R^{n\times n}$ which means that we have the conjugate pair eigenvalue $\lambda_{\pm}=\rho \pm i\omega$ with eigenvectors $v,\overline{\v}$

Consider the two dimensional case $A$ with only two eigenvalues.

Let $Q=[\text{re}(v),\text{im}(b)]$ note that we can express $v, \overline{v}$ interms of these:
$$\begin{align}
AQ=[re(Av),Im(Av)]\\
=[re(\lambda v), im(\lambda v)]
\end{align}$$
now note that $\lambda = \rho + i\omega, v= re(v)+i im(v)$
$$\begin{align}
=[\rho re(v)-\omega im(V),\omega Re(v)+\rho im(v)]\\
=Q[[\rho,-\omega],[\omega , \rho]]
\end{align}$$
We call this the real canonical form of the matrix A

$$\begin{align}
Q^{-1}AQ=[[\rho -\omega],[\omega \rho]]\\
=\begin{bmatrix}
\rho & 0\\ 0 & \rho
\end{bmatrix}\begin{bmatrix}0&-\omega\\\omega & 0\end{bmatrix}\\
= \Rho +\Omega
\end{align}$$
So we know that:
$$\begin{align}
e^{(\Rho+\Omega)t}=e^{\Rho t}e^{\Omega t}\\
\end{align}$$
So we have exponential increase or decay for one part. Now take $e^{\Omega t}$
$$\begin{align}
\Omega^{2n}=-1^n[[\omega^{2n},0],[0,\omega^2n]]\\
\Omega^{2n+1}=(-1)^{n}[[0,-\omega^{2n+1}],[\omega^{2n+1},0]]\\
e^{\Omega t}=[[\sum\limits_{k=0}^{\infty}\left((-1)^n\right)\omega^{2n}t^{2n}/(2n)!,-\sum\limits_{k=0}^{\infty}\left((-1)^n \frac{\omega^{2n+1}t^{2n+1}}{(2n+1)!}\right)]]
\end{align}$$
And similarly for the bottom portion
$$\begin{align}
e^{\Omega t}=\begin{bmatrix}
\cos(\omega t)&-\sin(\omega t)\\
\sin(\omega t)&\cos(\omega t)
\end{bmatrix}
\end{align}$$
So the exponential of this matrix is literally a rotation matrix.

In the first situation $\rho = 0,\omega > 0$, This is a circle. If $\omega < 0$ then the rotation is clockwise as opposed to counter clockwise

Second situation $\omega,\rho > 0$ or $\omega < 0,\rho > 0$ This is an outward spiral

Lastly if $\omega,\rho < 0$ or $\rho < 0,\omega > 0$ then this is an inward spiral.

## Combining both
Say we have n distinct eigenvalues with some complex. If $A$ has n distinct eigenvalues real or complex. let the eigenvalues be $\lambda_1,\dots,\lambda_k,\lambda_{k+1},\overline{\lambda_{k+1}},\dots$ Where these are all distinct. The first $k$ real and the last $2l$ complex. Eigenvectors $u_1,\dots,u_k,re(v_{k+1}),im(v_{k+1}),\dots u_l,v_l$. Call this matrix Q.

$$\begin{align}
Q^{-1}AQ=\Lambda+\Omega
\end{align}$$
Where Lambda is diagonal up to a point and then the omegas take over with the canonical form.

We will do jordan canonical form next time.
# Next day
First we talked about the exponential of a diagonal matrix, then the exponential of a diagonalizable matrix, then that with complex eigenvalues (rotation matrix)
$$\begin{align}
\lambda_1,\dots,\lambda_k, \lambda_{k+1},\overline{\lambda_{k+1}}
\end{align}$$
So there exists a matrix Q with:
$$\begin{align}
Q^{-1}AQ=[\lambda_1,\dots,\lambda_k, D_1,\dots,D_l]
\end{align}$$
The eigenvectors tell us how oval the shape of the complex circles are.
## Degenerate Eigenvalues

The eigenvalues are the roots of the characteristic polynomial
$$\begin{align}
0=\det(A-\lambda I)=\prod(\lambda-\lambda_j)
\end{align}$$
These can be complex and repeated

Algebraic multiplicity, $\alpha(\mu)$ of $\mu$ eigenvalue is the order of the root $\mu$

Define the eigenspace of $\mu$ to be the kernel of $A-\mu I$. The dimension of the eigenspace is the geometric multiplicity of $\mu$.

The geometric multiplicity is always less than or equal to the algebraic multiplicity.

### Jordan Canonical Form
We only state the conclusion, without the proof.

When the Algebraic multiplicity is greater that the geometric multiplicity and the algebraic multiplicity is k.

Let $v$ be a vector satisfying:
$$\begin{align}
(A-\mu I)^kv=0
\end{align}$$
define Q:
$$\begin{align}
Q=[v,(A-\mu I)v,\dots, (A-\mu I)^{k-1}v]
\end{align}$$
then:
$$\begin{align}
Q^{-1}AQ= % 2 x 3 BMatrix
\begin{bmatrix}
\mu & 1 & 0 \\
0 & \mu & 1 \\
0&0&\mu
\end{bmatrix}
\end{align}$$

Lets talk about $e^{At}$. Consider 2x2 situation first with a degenerate eigenvalue.
$$\begin{align}
A= % 2 x 2 BMatrix
\begin{bmatrix}
\lambda & 1 \\
0 & \lambda
\end{bmatrix}
\end{align}$$
We want to compute $e^{At}$
$$\begin{align}
e^{At}=e^{\lambda It + Nt}=e^{\lambda It}e^{Nt}
\end{align}$$
N is a nilpotent matrix so take the exponential $N^2=0$:
$$\begin{align}
e^{At}= % 2 x 2 BMatrix
\begin{bmatrix}
e^{\lambda t} & 0 \\
0 & e^{\lambda t}
\end{bmatrix} % 2 x 2 BMatrix
\begin{bmatrix}
0 & t \\
0 & 0
\end{bmatrix}\\
% 2 x 2 BMatrix
\begin{bmatrix}
e^{\lambda t} & te^{\lambda t} \\
0 & e^{\lambda t}
\end{bmatrix}
\end{align}$$
Degenerate eigenvalues result in polynomial behavior

in a $k\times k$ it will result in a $(k-1)^{\text{th}}$ order polynomial behavior.

so:
$$\begin{align}
x(t)=e^{At}x_0\\
=P(t)e^{\lambda t}e_1+P'(t)e^{\lambda t}e_2+\dots+P^{(k-1)}(t)e^{\lambda t}e_k\\
x_0= [x_0^0,x_0^1,\dots]\\
P(t)=x_0^0+x_0^1t+\dots x_0^{k-1}\frac{t^{k-1}}{(k-1)!}
\end{align}$$
Degeneracy results in polynomial effects c

What if the jordan block has complex eigenvalues?
$$\begin{align}
% 4 x 4 BMatrix
\begin{bmatrix}
D_1 & I & 0 & 0 \\
0 & D_1 & I & 0 \\
0 & 0 & D_1 & I \\
0 & 0 & 0 & D_1
\end{bmatrix}
\end{align}$$
Where the identities are $2\times 2$

As before we can seprate:
$$\begin{align}
e^{At}=e^{\rho It}e^{Dt}e^{Nt}
\end{align}$$
The solutions are of the form:
$$\begin{align}
x_k(t)=P_1^{(k-1)}(t)e^{\rho t}cos(\omega t)+P_2^{k-1}(t)e^{\rho t}\sin(\omega t)
\end{align}$$
$P_1, P_2$ are polynmoials ofr order at most L-1. The superscripts here are derivatives.
