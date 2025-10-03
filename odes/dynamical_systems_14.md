# Concepts of Dynamical Systems

- A dynamical system is the action of a semi group G with identity element e on a set M. That is a mapping

$$\begin{align}
T:G\times M\rightarrow M\\
(g,x)\rightarrow T_g(x)
\end{align}$$
which respects the semi group property
$$\begin{align}
T_g\circ T_h=T_{gh}\\
T_e=I
\end{align}$$
Semi group does not necessarily have an inverse

### Examples:
Discrete dynamical systems with:
$$\begin{align}
G=\mathbb Z \text{ group}
\end{align}$$
or $G=\{0,1,2\}$ (semi group)

Continuous dynamical system $G=\R$ (Group) or $G=[0,\infty)$ (Semi group)

- Example 1:
Flow map for an autonomous ODE on $\R^n$ is a continuous time dynamical system on $\R^n$ parameterized by $\R$ (the time)

- Example 2:
The application of the monodromy matrix for a time periodic linear system
$$\begin{align}
\dot{x}= A(t)x\\
x_0\rightarrow M^Tx_0
\end{align}$$
This is a discrete dynamical system parameterized by $\mathbb {Z}$

- Example 3:
The application of a continuous mapping $f$ on a subset $X$ of a Banach Space $x\rightarrow f(x)$ this is a discrete dynamical system. Parameterized by $\mathbb N_0$

$$\begin{align}
x_{n+1}=rx_n(1-x_n)\\
\dot{x}=rx(1-x)
\end{align}$$

Recall: Flow map

Nonlinear autonomous ODE systems on $\R^n$ $\dot{y}=f(y)$ if this is globally lipshitz. Then the flow map is defined as:
$$\begin{align}
\phi_t(x) \text{ solve the equation with } \phi_0(x)=x
\end{align}$$
Define orbitals or trajectories of the flow map as $\Gamma(x)=\bigcup_{t\in \R}\{\phi_t(x)\}$.

The forward and backward trajectories from a point $x$ are $\Gamma_\pm(x)=\bigcup_{\pm t>0}\{\phi_t(x)\}$

## Remark:
if $\Gamma(x)=\{x\}$ that means that $x$ is a fixed point or a stationary point of the flow

Extension. A point $x\in \R^n$ is called a periodic point if there is $T>0$ such that $\phi_t(x)=x$. That means that if $x\in \Gamma_t(x)$ in this case $\Gamma(x)$ is called a periodic orbital or a closed orbit.
## Lemma: IF one point is periodic than all of the points are periodic
if $\Gamma_+(x)\cap \Gamma_-\neq \empty$ then $x$ is a periodic point.

Moreover if one point on the orbit is periodic then all points on the orbit are periodic. (Use uniqueness)

## Invariant sets
A set $E\subset \R^n$ is called positively invariant if
$$\begin{align}
\Gamma_+(x)\in E,\forall x\in E
\end{align}$$
similarly for negatively invariant. If its both negative and positively invariant then it is just plain invariant.

There are some properties of the invariant set that we care about.
- Arbitrary intersections of positively invariant sets are positively invariant (Proof of this is trivial.)

Pf: if $x\in E_\alpha$ the intersection of all positively invariant sets. then $\Gamma_+(x)\subset E_\alpha$ for all $\alpha$. then $\Gamma_+(x)\subset E_\alpha$ for all $\alpha$
- The closure of a positively invariant set is positively invariant. We need to use the fact that the flow is continuous

pf: Let $E$ be positively invariant. and let $x\in \overline{E}$ we  want to show $\Gamma_+(x)\in X$. there is a sequence $x_n\in E\rightarrow x$ and $\Gamma_+(x_n)\in E$ then $\forall t>0$ $\phi_t(x_n)\rightarrow \phi_t(x)$ as $n\rightarrow \infty$ this means that $\phi_t(x)\in \overline{E}$. That means that $\Gamma_+(x)\in \overline{E}$

- If $E$ and $F$ are invariant then $E-F$ is invariant

pf let $x\in E-F=E\Cap F^C$ so x is in E but not in F. This follows easily from intersection of sets

## Omega positive sets
$$\begin{align}
\omega_+=\overline{\Gamma_+}\\
\omega_-=\overline{\Gamma_-}
\end{align}$$
