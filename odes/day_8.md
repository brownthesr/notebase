
# Constant coefficient linear systems

We are going to study $\dot x =Ax$ with $x(0)=x_0$ where $x(t)\in \R^n$ and $A\in \R^{n\times n}$

consider linearizing $\dot{x} = f(x)$

Suppose $f:\R^n\rightarrow \R^n$ is $C^1$, $f(0)=0$ consider $\dot{x}=f(x), x(0)=\epsilon y_0$ ($\epsilon<<1$):
$$\begin{align}
\dot{x} = Df(0)x+O(x^2)
\end{align}$$
since $\epsilon$ is small then we can consider neighborhoods close to zero:
$$\begin{align}
\dot x = Df(0)x
\end{align}$$
Solution. let $x(t)=\epsilon y(t)$ then:
$$\begin{align}
\dot y(t)= \frac{1}{\epsilon}f(\epsilon y)=\frac{1}{\epsilon}(f(0)+\epsilon Df(0)y+O(\epsilon^2))\\
\approx Df(0)y
\end{align}$$
So the linearized system is :
$$\begin{align}
\dot y = Df(0)y\\
y(0)=y_0
\end{align}$$
## Solution
$x(t)=x_0e^{At}$ normally
### Definition
if $A\in M^{n\times n}$ matrix (not necessarily real) we define the matrix exponential to be:
$$\begin{align}
e^{A}=\sum\limits_{k=0}^{\infty}\left(\frac{A^k}{k!}\right)
\end{align}$$
### Remark
Convergence?
$||A||_{\text{op}}=\sup_{x\neq 0}\frac{|Ax|}{|x|}$. This automatically satisfies submultiplicativity:
$$\begin{align}
||\sum\limits_{k=0}^{\infty}\left(\frac{A^k}{k!}\right)||\\
\leq \sum\limits_{k=0}^{\infty}\left(\frac{||A||^k}{k!}\right)\\
=e^{||A||}
\end{align}$$

Question:
$$\begin{align}
e^{A}e^{B}=e^{A+B}
\end{align}$$
not necessarily, only if $AB=BA$

Furthermore $(e^{A})^{-1}=e^{-A}$ because $A$ commutes with $e^{-A}$

We now justify this solution.
### Solution matrix of a linear system:
The matrix exponential $e^{At}$ is itself a matrix solution of the linear system. $\dot x = Ax, x(0)=I$
$$\begin{align}
\frac{d}{dt}(e^{At})=\frac{d}{dt}\sum_{k=0}^\infty \frac{A^kt^k}{k!}\\
=\sum\limits_{k=0}^{\infty}\left(A^kt^{k-1}/(k-1)!\right)\\
=Ae^{At}
\end{align}$$
So it is a solution.

## Flow map
The matrix exponential explicitly identifies the flow map for the ODE $\dot{x} = Ax$ $\phi_t(x_0)=e^{At}x_0$ as the solution of
$$\begin{align}
\frac{d}{dt}\phi_t(x_0)=A\phi_t(x_0), \phi_0(x_0)=x_0
\end{align}$$

## Duhamels principle

$$\begin{align}
\dot{x}=Ax+f(t)
\end{align}$$
with $x(0)=x_0$
The solution if given by:
$$\begin{align}
x(t)=e^{At}x_0+\int_0^te^{A(t-s)}f(s)ds
\end{align}$$
To prove this we take the integrating factor $e^{-At}$
$$\begin{align}
e^{-At}\dot x(t)-e^{-At}Ax(t)=e^{-At}f(t)
\frac{d}{dt}(e^{-At}x)=e^{-At}f(t)\\
e^{-At}x=\int_0^te^{-As}f(s)ds+x_0\\
x=\int_0^te^{A(t-s)}f(s)ds+e^{At}x_0\\
\end{align}$$

## Diagonal System
Then we know that $\dot x =\Lambda x$ then
$$\begin{align}
x(t)=e^{\Lambda t}x_0
\end{align}$$
We can just take it componentwise

### Special case $n=2$
$$\begin{align}
\lambda,\mu
\end{align}$$
$$\begin{align}
\lambda=\mu <0
\end{align}$$
then everything will converge to zero at the same speed. In the phase plot. If one is lower than the other then it converges to zero faster.
