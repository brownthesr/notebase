# First day of Class

He wants us to high pass the course. Just through homework and final exams.

Textbook should be available online.

## Course Breakdown

- 50% is in homework.
- 50% on final exam.
- A is 90% (High Pass)
- A- is 85-90
- B+ is 80-90 (Pass)

## What we will study

- IVP (Existence and Uniqueness)
- Linear Equations (Matrix Exponentials)
  - Duhamels Principle, variation of parameters
- Dynamical Systems Theory (Geometric Methods, Nonlinear Problems)
- Pertubations Methods
- BVPs (optional)

## A few Examples (May be put in exam)

Optimization:

1. Minimize $f(x), x\in \R^d$

- Gradient Descent $x^k=x^{k-1}-s\nabla f(x^{k-1})$

if we let $s\rightarrow 0$ then
$$
\frac{x^k-x^{k-1}}{s}=-\nabla f(x^{k-1})\\
$$
let $x^k=X(ks)$ then:
$$
\dot X(t)=-\nablda f(X(t))
$$
if $f(x)$ is convex, then $f(X(t)) - f^\star\leq \frac{C}{t}$ (Prove ****** )

- Poliak $\ddot X(t)+r\dot X(t)=\nabla f(X(t))$
- Nesterov $\ddot X(t) + \frac{3}{t}\dot X(t)=-\nabla f(X(t))$, implies that $f(X(t))-f^\star\leq \frac{C}{t^2}$ (Prove it!)

2. Generative Modeling
$p(x)$

Probability flow ODE. (We won't necessarily prove this in this class)
$$\begin{align}
\dot X = f(x,t)-\frac{1}{2}\beta(t)\nablda \log(p_t(X))
\end{align}$$

## IVPs
IVP for a first order system: find $x(t): [0,T]\rightarrow \R^n$ that solves $\dot x = f(t,x(t)), x(0)=x_0$

Where f is continuous and U is open $f:U\rightarrow \R^n$ and $x_0\in U$

## General Higher order ODE (We can typically convert these to lower order systems, remember to apply implicit function theorem.)
$F(t,y,y',\dots, y^{(k)}) = 0$ for $t\geq 0$)

How to convert it to an IVP.

Apply implicit function theorem, if $\partial y_k F\neq 0$ then there is a small neighborhood of zero that you can write $y^k(t)=g(t,y(t),\dots, y^{k-1}(t))$

let $x(t)=[y,y',...,y^{k-1}], \dot x$ is you know. Then set $f(t,x)=[x_2, x_3,\dots, g(t,x_1,\dots,Textbook)]$

# Existence of Solution (Is there a solution)
- $\dot x = x^2$ (This has only a local solution, we will come back to this)

Local: Exists in a small interval around initial time.
Global: For all positive times.

Typically you use the contraction mapping principle.
We can't just use existence we also need uniqueness
## Uniquness
Is there only one solution?

We also study regularities of solutions: Basically dependence on data and regularity of the dependence on the equation. (Well Posednessh)

- Long time/asymptotic behavior of solution

- Bifucation
- Perturbation theorem
