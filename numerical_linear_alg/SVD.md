# SVD

If A is a square matrix it always has n eigenvalues, if we are lucky it has n linearly independent eigenvectors. A is hermitian iff it is unitarily real diagonalizable.

Question: Hermitian and skew hermitian matrices are diagonalizable. What are all the class of matrices?

In our proof strategies. If v is an eigenvector of A then we require that the orthogonal compliment is an invariant subspace (look at the deflation strategy).

The idea is we needed if $v$ is an eigenvector of $A$ then it is also an eigenvector of $A^*$. What we need is that $A$ and $A^*$ need to have the same eigenvectors. This is a pretty strong assumption

Fun surprising fact, two square matrices $A,B$ have the same eigenvectors iff $AB=BA$ (The idea is that the invariant subspaces are the same). So A must commute with its hermitian.

It turns out that matrices are diagonalizable iff they are normal;

## Definition: Normal

$$\begin{align}
A^*A=AA^*
\end{align}$$
This is a pretty strong condition. example:
$$\begin{align}
A = [[1,0],[0,i]]
\end{align}$$

## Theorem: The spectral theorem
A matrix is normal iff they are unitarily diagonalizable

Normal matrices are the class of matrices for which the eigenvalues precisely characterize the action of the matrix. Everything that you wish was true about eigenvalues is.

Clean way: Use the schur decomposition
$$\begin{align}
A^*A=AA^*\\
UT^*U^*UTU^*=UTU^*U^*T^*U\\
U^*T^*U^2TU^*=UT(U^2)^*T^*U\\
U^*U^*T^*UUTU^*U^*=TU^*U^*T^*
\end{align}$$
if T was invertible then we could get that T was diagonal
$$\begin{align}
UU(T^*)^{-1}U^*U^*T^*UUTU^*U^*=T
\end{align}$$

So to prove this take the schur decomposition and assume that A is normal:
$$\begin{align}
A=UTU^*\\
\end{align}$$
Then:
$$\begin{align}
A^*A=AA^*\\
UT^*U^*UTU^*=UTU^*UT^*U^*\\
UT^*TU^*=UTT^*U^*\\
T^*T=TT^*
\end{align}$$
So T must be normal. We now prove that any normal upper triangular matrix must also be diagonal...
take $e_1$:
$$\begin{align}
T^*Te_1\\
=T^*[T_{11},0,\dots].T\text{ since T is upper trinagular}\\
=[|T_{11}|^2,0,\dots].T
\end{align}$$
but in addition:
$$\begin{align}
TT^*e_1\\
=T[ \overline{T_{11}}, \overline{T_{12}},\dots].T\\
=[\sum_j |T_{1j}|^2,\dots].T
\end{align}$$
Note I left off the last n-1 entries of the vector because we will not be using them.

Now note that since these two must be equal we know that $\sum |T_{1j}|^2=|T_{11}|^2$. Thus $T_{1j}=0$ for $j\neq 1$. From this we immidiately get equality above.

Now that we have established that as a base case we prove assume that $T$ is normal and diagonal up to k and prove it is diagonal on $k+1$ or that $T_{k+1,j}=0$ for $j>k+1$ to do this take the vector $e_{k+1}$ then:
$$\begin{align}
T^*Te_{k+1}\\
=T^*[0,\dots,T_{k+1,k+1},0,\dots].T \text{ because of inductive hypothesis all rows above are zero}\\
=[0,\dots, |T_{k+1,k+1}|^2,0,\dots].T
\end{align}$$
Furthermore
$$\begin{align}
TT^*e_{k+1}\\
=T[0,\dots \overline{T_{k+1,k+1}}, \overline{T_{k+1,k+2}},\dots].T\\
=[0,\dots, \sum_{j=k+1}^n|T_{k+1,j}|^2,\dots].T
\end{align}$$
(Once again we ignore the last $n-k-1$ entries because we do not use them )

From here we then know that $\sum_{j=k+1}^n|T_{k+1,j}|^2=|T_{k+1,k+1}|^2$. So that must mean that $T_{k+1,j}=0$ for $j>k+1$.

Carry out this induction to n and we are left with the fact that $T$ is Diagonal.

From this we can see that $A=UTU^*$ where T is diagonal so A is unitarily diagonalizable.

In the opposite direction assume that A is unitarily diagonalizable then:
$$\begin{align}
AA^*=UDU^*UD^*U\\
=UDD^*U^*
\end{align}$$
Now remember that all diagonal matrices commute so:
$$\begin{align}
=UD^*DU^*\\
=UD^*U^*UDU^*\\
=A^*A
\end{align}$$
So A is normal. and it is proven

## Recall
- All non-effective square matrices are diagonalizable
- All square matrices are bidiagnalizable
- All square matrices are unitarily triangularizable
- All normal matrices are exactly the set of diagonalizable square matrices.

## SVD
All matrices are asymmetrically unitarily diagonalizable
$$\begin{align}
A=U\Sigma V^*
\end{align}$$

We have left and right singular vectors. The decomposition is unique up to unitary transformation in subspaces with equal singular values.

Prove Assume $m\geq n$. Then we know that $A^*A$ is positive semi definite and hermitian so it has an eigendecomposition with non-negative eigenvalues

$$\begin{align}
A^*A=V\Lambda V^*
\end{align}$$

set $u_i=\frac{1}{\sigma_i}Av_i$ for $\sigma_i=\sqrt{\lambda_i}$ for nonzero lambda. You can show that these vectors are in fact orthonormal, You can also complete them into a basis.

$$\begin{align}
u_j\sigma_j=Av_j
\end{align}$$
we also know that $u_j*0=Av_j$ for the rest of the singular vectors that are zero
$$\begin{align}
[u_1\dots u_n]\Sigma=AV\\
[u_1\dots,u_n,u_{n+1}\dots,u_m] % 2 x 1 BMatrix
\begin{bmatrix}
\Sigma \\
0
\end{bmatrix}=AV\\
U\Sigma V^*=A
\end{align}$$
## properties of SVD
$$\begin{align}
A=\sum_{j=1}^p \sigma_j(u_jv_j^*)
\end{align}$$
Every matrix is a rotation, diagonal scaling, then another rotation

Rank of the matrix is the number of nonzero singular values
$$\begin{align}
||A||_2=\sigma_1
\end{align}$$
if A is square and invertible then:
$$\begin{align}
A^{-1}=V\Sigma^{-1}U^*
\end{align}$$
Four fundamental subspaces.

If you are asked to find projectors onto these fundamental subspaces. Use the SVD.

## Question: how are the singular values related to the eigenvalues?
The number of zero eigenvalues is the number of zero singular values. Note much related

## Low rank approximation
We want to solve:
$$\begin{align}
\argmin_{\substack{B\in C^{m\times n}\\\text{rank}(B)\leq r}}||A-B|| \end{align}$$
For some norm. With $r< \min\{m,n\}$

## Definition
Unitarily invariant norms satisfy $||A||=||UAV||$. So the norm is only a function of its singular values.
$$\begin{align}
||A||=f(\sigma_1,\dots,\sigma_p)
\end{align}$$

## Theorem: Schmidt
if a norm is unitarily invariant then:
$$\begin{align}
B_k=\argmin ||A-B||
\end{align}$$
Then the solution is $B_k=\sum \sigma_ku_kv_k^*$. The solution is unique of $\sigma_k>\sigma_{k+1}$
## Computing the SVD
Just compute the eigenvalues of $A^*A$ then get $u_j=\frac{Av_j}{\sigma_j}$

So it comes down to computing eigenvalues. Specifically a normal one. We can do lots of things if we know about the eigenvalues. There are things we need for this:
- What makes a good computational algorithm?
- How do we solve a linear system?
- How to orthogonalize vectors?
