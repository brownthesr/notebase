# Stability and instability of autonomous linear systems

Consider the linear system
$$\begin{align}
\dot{x} = Ax
\end{align}$$
with eigenvalues $\lambda_1,\dots \lambda_k, \lambda_{k+1}, \overline{\lambda_{k+1}}, \dots \lambda_{k+l}$

With $\lambda_k=\rho_k+i \omega_k$ and generalized eigenvectors:
$$\begin{align}
w_j=u_j+iv_j
\end{align}$$
forming a basis of $\R^2$

$$\begin{align}
B=\{u_1,\dots, u_k, w_{k+1}\dots\}
\end{align}$$
Define the following.
- Stable subspace $E_s=$space of eigenvectors spanned by the eigenvectors that have eigenvalue real part less than zero.
- Unstable zero:$E_u=$space of eigenvectors spanned by eigenvalues with real part greater than zero.
- Center Subspace: $E_c=$ space of eiegenvalues with eigenvalues that have zero real part.

Example:
$$\begin{align}
\dot x = Ax
\end{align}$$
where $% 3 x 3 BMatrix
\begin{bmatrix}
0 & -1 & 0 \\
1 & 0 & 0 \\
0 & 0 & -1
\end{bmatrix}$
Notice that this is a block diagonal. The first block is already in reduced form. The second is as well. So the center space is literally just the span of $e_1,e_2$ where the stable space is $e_3$

## Theorem: Invariant Subspaces
Let $A\in \R^{n\times n}$ then $\R^n=E_s\oplus E_n \oplus E_c$ and the subspaces are all invariant under flow.

Proof:
Let us first check $AE\subset E$ where E is one of those subsets of the generalized eigenspace associated with eigenvalue $\lambda$. Iv $v\in E$ then $\exists k$:
$$\begin{align}
(A-\lambda I)^kv=0
\end{align}$$
then:
$$\begin{align}
(A-\lambda I)^{k-1}(A-\lambda I)v=0
\end{align}$$
so then $(A-\lambda I)v\in E$ so $Av\in \lambda v+E=E$ so $AE\subset E$

But we want to show that $e^{At}E\subset E$. The idea is to use limits and subsets.

take $e^{At}v$ we want to show this is in E.
$$\begin{align}
e^{At}v=(\lim_{k\rightarrow\infty} I+At+\dots+\frac{(At)^k}{k!})v\\
=(\lim_{k\rightarrow\infty} Iv+Avt+\dots+\frac{(At)^kv}{k!})
\end{align}$$
Clearly by induction each entry here is in $E$. So for any fixed k. This is a vector in $E$. Since E is closed because it is finite dimensional subspace, then this limit is also in $E$.

So it is proved for any of these subspaces.

## Theorem: Stability
The following are equivalent:
1. All eigenvalues of A have negative real part
2. For all $x_0\neq 0$ then $\lim_{t \rightarrow \infty}e^{At}x_0=0$ and $\lim_{t \rightarrow -\infty}|e^{At}x_0|\rightarrow \infty$
3. There are constants $M,m, a,b$ that are all positive such that $\forall t>0, |e^{At}x_0|\leq Me^{-at}|x_0|$.
3. for all $t<0$ then $|e^{At}x_0|\geq me^{-bt}|x_0|$
### Remark
The stationary solution at 0 is asymptotically stable. In that all solutions converge to zero.
## Theorem: Stable/Unstable subspace.
<!-- NOTE: This may be on the exam -->
- For a real matrix A there are constants $M,m,a,b$ positive such that $\forall x_0\in E_s$ and all $t>0$, $|e^{At}x_0|\leq Me^{at}|x_0|$
- for all $x_0\in E_u$ and all $t>0, |e^{At}x_0|\geq me^{bt}|x_0|$
- For all $x_0\in E_c$ we have $|e^{At}x_0|\leq M(1+t^k)|x_0|$. Where k is the difference between algebraic multiplicities and geometric multiplicities.
- if $x_0\notin E_s\oplus E_c$ (so $E_u$ is nontrivial) then $|e^{At}x_0|\rightarrow \infty$

I prove these myself.: So because each subspace is invariant under flow it suffices to consider the cases of a matrix A being only in that subspace.

Assume that for a matrix A we have that all of the eigenvalues have real part less than zero then take:
$$\begin{align}
||e^{At}x_0||\leq |e^{At}||x_0|\\
=|x_0||V||V^{-1}||e^{Jt}|
\end{align}$$
for some set of jordan blocks $J$ from here note tjhat:
$$\begin{align}
=M|x_0||e^{\Lambda t}e^{Nt}|\\
\leq M|x_0||e^{\Lambda t}|\sum_{k=0}^{n-1}\frac{t^k}{k!}||N^k||
\end{align}$$
from here remember that the norm of a diagonal matrix is the largest real part so:
$$\begin{align}
\leq M |x_0|e^{\text{re}(\lambda_j)}\sum_{k=0}^{n-1}\frac{t^k}{k!}||N^k||
\end{align}$$
Now remember that polynomials are always bounded above by the any exponential namely we can always choose $K_p$ such that $Ke^{pt}\geq P$. choose $p=-\lambda_j/2$ . then:
$$\begin{align}
\leq M|x_0|e^{-\alpha t}K_pe^{\alpha_2t}\\
\leq P|x_0|e^{-\alpha/2 t}
\end{align}$$
and it is proven.

To prove this remember that $|A||A^{-1}|\geq 1$ so $|A|\geq 1/|A^{-1}|$
so we have:
$$\begin{align}
|e^{At}x_0|\geq|x_0||e^{At}\frac{x_0}{|x_0|}|\geq  \frac{|x_0|}{|e^{-At}|}\geq |x_0|\frac{1}{P}e^{\alpha t}
\end{align}$$

For the final case we will note that we can no longer bound the nilpotent matrix by an exponential. However since there are no exponentials anywhere (The norm of the matrix is just one). We can bound it by  a polynomial instead.

# Nonlinear stability of fixed point:
Consider a nonlinear autonomous system $\dot x = f(x)$. With $f$ smooth and $f(0)=0$. If all of the eigenvalues of $Df(0)$ have strictly negative real part. Then the fixed point at 0 is said to be  linearly stable. In a small neighborhood it should go to zero.
## Theorem:
Suppose $f$ is smooth and $f(0)=0$ and all eigenvalues of $Df(0)$ have negative real part. Then there is a $\delta,\alpha >0$ such that any solution of $\dot{x}=f(x),x(0)=x_0$ with $|x_0|\leq \delta$ satisfies $|x(t)|\leq Ce^{-\alpha t}|x_0|$

Proof: Linearized problem. Originally we have $\dot{x}=f(x),x(0)=x_0$. The linearized problem is $x=\epsilon y$ so:
$$\begin{align}
\dot y = \frac{1}{\epsilon}(\dot x)\\
= \frac{1}{\epsilon}(f(x))\\
= \frac{1}{\epsilon}(f(y\epsilon))\\
= \frac{1}{\epsilon}(f(0)+Dfy\epsilon +O(\epsilon^2))\\
\approx \frac{1}{\epsilon}(f(0)+Dfy\epsilon +O(\epsilon^2))\\
\end{align}$$
or we could do
$$\begin{align}
\dot x = f(x)=f(0)+Df(0)x+R(x)|x|\\
\approx Df(0)x+ R(x)
\end{align}$$
Where $R(x)$ approaches zero as x approaches zero. So this problem reduces to:
$$\begin{align}
\dot{x}=Df(0)x+R(x)||x||\\
x(0)=x_0
\end{align}$$
We can solve this using Duhamels principle. We can't just ignore the $R(x)$.

To apply Duhamels we get:
$$\begin{align}
x(t)=e^{Df(0)t}x_0+\int_0^te^{Df(0)(t-s)}R(x(s))ds\\
\leq Ke^{-\sigma t}|x_0|+\int_0^tKe^{-\sigma (t-s)}|R(x(s))|ds
\end{align}$$
Because of how small $R(x)$ can get we know that $|R(x)|\leq |x|\eta$ for $|x|\leq \delta_0$. So:
$$\begin{align}
\leq  Ke^{-\sigma t}|x_0|+\eta\int_0^tKe^{-\sigma (t-s)}|x(s)|ds
\end{align}$$
From here notice that if we multiply both sides by $e^{\sigma t}$:
$$\begin{align}
|x(t)|e^{\sigma t}\leq K|x_0|+\eta \int_0^t e^{\sigma s}|x(s)|dt
\end{align}$$
We can thus apply gronwalls to both sides to get:
$$\begin{align}
|x(t)|e^{\sigma t}\leq K|x_0| e^{\eta\int_0^t 1}\\
|x(t)|e^{\sigma t}\leq K|x_0| e^{\eta t}\\
|x(t)|\leq K|x_0|e^{(\eta-\sigma) t}\\
\end{align}$$
So long as we choose $\eta < \sigma$. Then both of these terms decay

We prove Duhamels principle:
$$\begin{align}
\dot{x} = A(t)x+g(t,x)
\end{align}$$
Where A is constant or periodic

## Remark
We call $\Phi(t)$ to be the principle matrix solution of $\dot x = A(t)x$. Define $\pi(t,s)=\Phi(t)\Phi(s)^{-1}$ (This is a map from s to t) This is the principle matrix solution started at time s. Assume that for some $c\geq 2$, $|\pi(t,s)|\leq Ce^{-\alpha(t-s)}$ for $t\geq s\geq 0$.

For this generalized problem
$$\begin{align}
\dot{x} = A(t)x+g(t,x)
\end{align}$$
we assume that $|g(t,x)|\leq b_0|x|$ (basically we know that this approaches zero) for $|x|\leq \delta$. We will prove that if $|x_0|\leq \frac{\delta}{c}$ and $b_0<<\alpha$ we have that:
$$\begin{align}
||x(t)||\leq De^{-(\alpha-b_0c)t}|x_0|
\end{align}$$
for $t\geq 0$ If we prove this then we proved the earlier thing.

Now we prove this. By Duhamels formula we have that:
$$\begin{align}
x(t)=\pi(t,0)x_0t+\int_0^t \pi(t,s)g(s,x(s))ds
\end{align}$$
let $\tau=\inf\{t>0:|x(t)|\geq \delta\}>0$, by the triangle inequality for $0\leq t\leq \tau$ we have that $x(t)\leq |\pi(t,0)||x_0|+\int_0^t ||\pi(t,s)|| ||g(s,x(s))||ds$ then:
$$\begin{align}
\leq Ce^{-\alpha t} ||x_0||+\int_0^t Ce^{-\alpha(t-s)}b_0 |x(s)|ds
\end{align}$$
multiply both sides by $e^{\alpha t}$ then:
$$\begin{align}
||x||e^{\alpha t}\leq C||x_0||+\int_0^t Cb_0e^{\alpha s}|x(s)|ds
\end{align}$$
From here we can directly apply gronwalls:
$$\begin{align}
||x||e^{\alpha t}\leq C||x_0||e^{\int_0^t Cb_0}ds\\
||x||e^{\alpha t}\leq C||x_0||e^{Cb_0t}ds\\
||x||\leq C||x_0||e^{-(\alpha-Cb_0)t}ds\\
\end{align}$$
Now the earlier problem follows since we can choose a delta for $R(x(s))<\frac{\alpha}{2C}$

<!-- NOTE: This will be on the exam -->
So we took a nonlinear prolem. Linearized it, then proved a more general theorem if we know that $g(x,t)\rightarrow 0$. Prove this again, as this will be important on the exam.

 e
