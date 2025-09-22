# Flow maps (Generative AI)

Maps a prior distribution to a posterior distribution.

Suppose $f$ is globally lipshitz continuous in $x$ and uniformly in $t$. Then by existence and uniqueness theorem we can define a flow map:
$$\begin{align}
\phi_t:\R^n\rightarrow\R^n
\end{align}$$
for each $x_0\in \R^n$, let $\phi_t(x_0)$ be the solution of
$$\begin{align}
\frac{d}{dt}\phi_t(x_0)=f(t,\phi_t(x_0))
\end{align}$$
With the initial condition
$$\begin{align}
\phi_0(x_0)=x_0
\end{align}$$
Suppose we have a bunch of mass and we want to minimize the transport (optimal transport). We need to design the flow map.

In generative modeling, I have an initial density (gaussian) I want to map it to target distribution, but I don't know it. However I can draw samples from it.

## Theorem: (Flow map regularity)
If $f(t,x)$ is lipshitz continuous in x with constant L than we know by gronwalls:
$$\begin{align}
e^{-Lt}|x_0-y_0||\phi_t(x_0)-\phi_t(y_0)|\leq e^{Lt}|x_0-y_0|
\end{align}$$
in particular the flow map itself is lipshitz with constant $e^{Lt}$

Properties of flow maps:
$$\begin{align}
\phi_0(v)=v \text{ (initial identity)}\\
\phi_{t+s}(v)=\phi_t(\phi_s(v)) \text{ (group property)}\\
\phi_{t}(\phi_{-t}(v))=v \text{ (inversion)}
\end{align}$$
Note that we can do this because its globally lipshitz

## Conserved Quantities (Invariant)
A quantity $H$ is called invariant under the flow if:
$$\begin{align}
H(\phi_t(v))=H(v)\\
\frac{d}{dt}H(\phi_t(v))=DH(\phi_t(v))\cdot f(\phi_t(v),t)=0
\end{align}$$

## Examples:
- The Lagrangian
- Energy in a system

Suppose $H(p,x)=\frac{1}{2}p^2+V(x)$. For newtons equation. This is invariant
$$\begin{align}
\dot p = -\nabla V(x)\\
\dot x = p
\end{align}$$
$$\begin{align}
% 2 x 1 BMatrix
\begin{bmatrix}
p \\
V'(x)
\end{bmatrix}\cdot % 2 x 1 BMatrix
\begin{bmatrix}
p \\
-V'(x)
\end{bmatrix}=0
\end{align}$$
A subset of the phase space $S\subset \R^n$ is called invariant if:
$$\begin{align}
\phi_t(S)\subset S
\end{align}$$
$\forall t\in \R$

Furthermore it is called positively (negatively) invariant if this holds for $t>0$ ($t<0$)

## Examples
- Any level set of an invariant quantity is invariant. For example the total energy of newtons equation.
- Invariant sets of $\frac{d}{dt}% 2 x 1 BMatrix
\begin{bmatrix}
x \\
y
\end{bmatrix}=% 2 x 1 BMatrix
\begin{bmatrix}
-x \\
y
\end{bmatrix}$

note that the solution is:
$$\begin{align}
y=y_0e^t,x=x_0e^{-t}\\
xy=x_0y_0
\end{align}$$
thus every level surface $xy=c$ in $\R^2$ is an invariant set.

### Another Example
$$\begin{align}
\frac{d}{dt} % 2 x 1 BMatrix
\begin{bmatrix}
x \\
y
\end{bmatrix}% 2 x 1 BMatrix
\begin{bmatrix}
y \\
-\frac{k}{m}x-\frac{\mu}{m}y
\end{bmatrix}
\end{align}$$
with the energy $H(y,x)=\frac{1}{2m}y^2+kx^2$

We then know that this H is invariant if $\mu=0$ it is positively invariant if $\mu>0$

Define the set $s=\{(y,x\in \R^2): H(y,x)\leq \lambda\}$ is positively invariant if $\lambda >0$ (This defines an ellipse)

## Question
How does $\phi_t$ change the volume of a set
$$\begin{align}
|\phi_t(\Omega)|=\int_\Omega |\det D\phi_t(x)|dx
\end{align}$$
Furthermore we know that:
$$\begin{align}
|A^{-1}|^n\leq \lambda_n^n\leq\prod \lambda_i=\det(A)=\prod \lambda_i\leq \lambda_1^n\leq |A|^n\
\end{align}$$
We then know that since the lipshitz:
$$\begin{align}
e^{-nLt}|\Omega|\leq |\phi_t(\Omega)|\leq e^{nLt}|\Omega|
\end{align}$$

Let $J(t,x)=\det(D\phi_t(x))$ then it satisfies the differential equation:
$$\begin{align}
\frac{d}{dt}J(t,x)=(\nabla\cdot f)(t,\phi_t(x))J(t,x)
\end{align}$$
and $J(0,x)=1$ just because the determinant of the identity is just 1.
<!-- NOTE: This will be in the exam -->
### Remark :
- if the divergence of f is zero then $J(t,x)=1$ and volume is preserved under the flow.
- if div is greater than zero then the volume increases
- vice versa for less than zero.
