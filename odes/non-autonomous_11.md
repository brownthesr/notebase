# Non-autnomous linear systems

$$\begin{align}
\dot{x}=A(t)x
\end{align}$$
## Construct the fundamental solution
For each standard basis vector $e_j$. Define $\phi_j$ to be the solution of $\dot{\phi}_j (t)=A\phi_j(t),\phi_j(0)=e_j$.

then the solution of $\dot x =A(t)x,x(0)=v$ is:
$$\begin{align}
x(t)=\Phi(t)v=v_0\phi_0(t)+\dots +v_n\phi_n(t)
\end{align}$$
This just follows from the linearity of the differential equation (plug it in if you doubt me). This is the fundamental matrix, Define
$$\begin{align}
\Phi(t)= % 1 x 3 BMatrix
\begin{bmatrix}
\phi_1(t) & \dots & \phi_n(t)
\end{bmatrix}
\end{align}$$
The matrix with the basis solutions $\phi_j(t)$ as the columns. This also called the fundamental solution or principle matrix.

Then the solution to the more general equation:
$$\begin{align}
\dot x = A(t)x\\
x(t_0)=x_0\\
\end{align}$$
Note that $\Phi(t)$ maps the point from the initial condition to its position at time t. So then $\Phi(t_0)$ maps from the point it is at at zero to its point at $t_0$ whereas the inverse maps $t_0$ to its point at the initial condition.

$$\begin{align}
x(t)=\Phi(t)\Phi^{-1}(t_0)x_0
\end{align}$$

## Variation of Parameters (Duhamels formula)
$$\begin{align}
\dot{x}=A(t)x+f(t)
\end{align}$$
Make the assumption that:
$$\begin{align}
x(t)=\Phi(t)c(t)
\end{align}$$
then:
$$\begin{align}
\dot x = A(t)\Phi(t)c(t)+\Phi(t)c'(t)\\
A(t)\Phi(t)c(t)+f(t)=A(t)\Phi(t)c(t)+\Phi(t)c'(t)\\
f(t)=\Phi(t)c'(t)\\
\dot{c}(t)=\Phi^{-1}(t)f(t)\\
\end{align}$$
So
$$\begin{align}
x(t)=\Phi(t)x_0+\int_0^t\Phi(t)\Phi^{-1}(s)f(s)ds
\end{align}$$
Which is the solution.
## Definition: Wronskian
Let $\Phi(t)=[\phi_1(t),\dots,\phi_n(t)]$ be the fundamental matrix solution associated with:
$$\begin{align}
\dot{\Phi}= A(t)\Phi
\end{align}$$
Then the wronskian is:
$$\begin{align}
W(t)=\det(\Phi(t))
\end{align}$$
Lioville/abel formula:
$$\begin{align}
\dot{W}(t)=tr(A(t))W(t)\\
W(t)=W(t_0)e^{\int_{t_0}^ttr(A(s))ds}
\end{align}$$
## Application: Sturm Lioville -type equation
$\ddot u+p(t) \dot{u}+q(t)u=0$. This can be rewritten as a first order system (we want to analyze the zeros of u)
$$\begin{align}
\frac{d}{dt} % 2 x 1 BMatrix
\begin{bmatrix}
u \\
\dot{u}
\end{bmatrix} = % 2 x 2 BMatrix
\begin{bmatrix}
0 & 1 \\
-q(t) & -p(t)
\end{bmatrix} % 2 x 1 BMatrix
\begin{bmatrix}
u \\
\dot{u}
\end{bmatrix}
\end{align}$$
The wronskian is given by. The trace is $-p(t)$ so:

Suppose that we have two solutions one $[u_1, \dot{u_1}]$ corresponding to $e_1$ and $u_2$ similar then the determinant is:
$$\begin{align}
u_1 \dot{u_2}-u_2 \dot{u_1}=W(0)e^{\int_0^t p(s)ds}
\end{align}$$
$$\begin{align}
|W(t)|=|u_1 \dot{u_2}-u_2 \dot{u_1}|=|W(0)e^{\int_0^t p(s)ds}|
\end{align}$$
So everything is always greater than zero if the initial conditions are linearly independent.

So if at some point either $u_1$ or $\dot{u_2}$ is zero then the other two cannot be zero

if $u_j(t)=0$ then $\dot{u_{j}}\neq 0$ and $u_{j+1}\neq 0$. With this we prove that the zeros are interlaced

Proof: assume that $u_1(a)=u_1(b)=0$. Then clearly $\dot{u_1},u_2\neq 0$ at those points. Then the sign of $\dot{u_1}$ are different signs. That means that since the Wronskian cannot change signs then $u_2$ has different signs. Since $u_2$ has different signs and it is continuous there must be a zero in between them.
