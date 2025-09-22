# Day 2

## Takeaways from last class

We can use change of variables and implicit function theorem to convert from a higher order ode to a system of odes that is mostly linear.

We also talked about from an optimization standpoint.

## Examples

A particle of mass $m>0$ at position $x(t)$ moves in $\R$ under a force field $F:\R\rightarrow\R$ and a frictional force ($\mu\geq 0$) opposing motion.

 we are considering a spring thing.

$$\begin{align}
m\ddot x=-\mu \dot x + F(x)
\end{align}$$
Note that this is a second order ode. We want to convert this to a first order system

Let $(x,p) = (x,m\dot x)$  from this we get
$$\begin{align}
\dot x = \frac{1}{m}p
\dot p= \frac{-\mu}{m}p+ F(x)
\end{align}$$

To do the energy based method, multiply the ode by $\dot x$
$$\begin{align}
m\ddot x \dot x - \dot x F(x)=-\mu \dot x^2\\
\frac{d}{dt} (\frac{p^2}{2m}+V(x)) = -\mu \dot x^2
\end{align}$$
where $V(x)=\int_0^xF(u)du$

### Remark
The quantity inside the derivative is conserved if $\mu = 0$, otherwise it decays.

This is called the hamiltonian, we will be asked to prove this (just take the derivative).

Remember the hamiltonian is kinetic energy plus potential energy.

### Remark
if $\mu = 0$ then the solution to this spring system (newtons equation) exists on the level sets of the hamiltonian

going back to the hamiltonian view point then this is equivalent to the system
$$\begin{align}
\dot x = \frac{\partial H}{\partial p}(p,x)
\dot p = -\frac{\partial H}{\partial x}(p,x)
\end{align}$$

## Next example (Ideal point mass on spring with spring constant $\kappa$) at rest state 0
$$\begin{align}
H(p,x)=\frac{1}{2}\kappa x^2 + \frac{p^2}{2m}
\end{align}$$
plots the phase diagam of x axis x and y axis p (I believe that we will be asked to do this)

These will be elipses. If we have $\mu > 0$ then we will have spirals towards zero.
## Pendulum Example
Ideal pointmass m hanging on a string of length $i$ and $\theta$ is the angle from the vertical axis. We are going to write the hamiltonian
$$\begin{align}
H(p,\theta) - \frac{p^2}{2m}+2mgL(1-\cos \theta)
p = mL\dot \theta
\end{align}$$
Plotting this as a phase diagram will be homework
## Population Dynamics
$$\begin{align}
\dot N = rN
\end{align}$$
Where r is the population growth rate, this is exponential.

A more realistic model is the logistic growth model:
$$\begin{align}
\dot N = \gamma N(1-\frac{N}{k})
\end{align}$$
Where k is the maximum capacity of the system. We want to understand the qualitative behavior of this

phase line analysis. Plot the positive and negative regions of the right hand side. Basically just find the zeros. This has two zeros (0,k) in between 0 and k the derivative is positive.

Qualitatively the solutions converge to critical points where the forcing point is zero and the stationary solutoin of the ode is 0 or k based on where the inital data sits. (We will prove this rigourously)

## Forcing model
$$\begin{align}
\dot N = r(10 \frac{N}{k})-H
\end{align}$$
now note that both zeros depend on H, for $H< \frac{\gamma k}{4}$ there are two positive fixed points where $r(10 \frac{N}{k})-H=0,\implies N\pm = \frac{(r\pm \sqrt r^2-\frac{4Hr}{k} )k}{2r} $

We can even plot the roots as a function of H

## Chemical Reaction
Suppose that we have two reactants A and B
$$\begin{align}
A+B\implies AB
\end{align}$$
Both of these directions are moderated by $k_1$ or $k_2$

Suppose that $n_x(t)$ is the density of x.

$$\begin{align}
\dot n_{AB}(t)= k_1n_A(t)n_B(t)-k_2n_{AB}(t)\\
\dot n_A(t)=\dot n_B(t)=k_2n_{AB}(t) - k_2n_A(t)n_B(t)
\end{align}$$
o
# Existence and Uniqueness
## Example
$$\begin{align}
\begin{cases}
\dot x = x^\frac{1}{3}
x(0)=0
\end{cases}
\end{align}$$
j

Note that one solution is definitely $x=0$. Another could definitely be $\frac{dx}{x^{1/3}}=dt$

$$
x^{2/3}\frac{3}{2}=t\\
x=t^{3/2}(\frac{2}{3})^{3/2}
$$
We need to think about this till after class. Note the solutions are just piece wise connections of our two solutions.
