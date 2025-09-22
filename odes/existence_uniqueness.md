# Day 3

## Remark

For an autonomoous ode if $x(t)$ is a solution then so is $x(t-t_0)$

So the general solution is:
$$\begin{align}
% 2 cases
\begin{cases}
0 \text{ if } t\leq t_0\\
\pm (\frac{2}{3}(t-t_0))^{3/2} \text{ if } t> t_0
\end{cases}
\end{align}$$

## Example 2, failure of global existence

$$\begin{align}
% 2 cases
\begin{cases}
\dot x = x^2 \text{ if } t>0\\
x(0)=x_0 > 0
\end{cases}
\end{align}$$

$$\begin{align}
\frac{dx}{x^2}=dt\\
\frac{-1}{x}=t+C\\
x=\frac{-1}{t+\frac{-1}{x_0}}
\end{align}$$

$$\begin{align}
% 2 x 2 BMatrix
\begin{bmatrix}
x_{11} & x_{12} \\
x_{21} & x_{22}
\end{bmatrix}% 2 x 1 BMatrix
\begin{bmatrix}
2 \\
x_{21}
\end{bmatrix}% 2 x 3 BMatrix
\begin{bmatrix}
x_{11} & x_{12} & x_{13} \\
x_{21} & x_{22} & x_{23}
\end{bmatrix}
\end{align}$$

## theoretical guarantees

First we consider the integral form of IVP.

Suppose we have a solution of:
$$\begin{align}
% 2 cases
\begin{cases}
\dot x = f(t,x) \text{ if } t\in (0,T)\\
x(0)=x_0
\end{cases}
\end{align}$$
Suppose that f is a $C^1$ function and satisfies the differential equation pointwise.  

BY FTC:
$$\begin{align}
% 2 cases
x(t)=x_0+\int_0^t \dot x(s)ds\\
x(t)=x_0+\int_0^t f(s,x(s))ds
\end{align}$$

We say $x\in C([0,T]\rightarrow R)$ is a solution of the integral form of the ivp if  it satisfies the integral form.

If $x(t)$ solves the Integral form then since $f(s,x)$ is a continuous function then $x(t)$ must be differentiable and we know that the derivative satisfies the original IVP.

Therefore these two problems are equivalent.

## Remark
if $x(t)\in C[a,b]$ and solves the IVP except possibly at $t_0\in (a,b)$ then $x$ solves the ode on the whole interval

Based on the integral form then:
$$\begin{align}
x(t)=x_0+\int\limits_{0}^{t}f(s,x) ds \text{ for }a\leq t<t_0\\
x(t)=x(t_0)+\int\limits_{t_0}^{t}f(s,x) ds \text{ for }a\leq t>t_0
\end{align}$$
Based on continuity that allows us to combine these to the whole interval.
## Lemma (solution concatenation)
If x is a solution of $\dot x=f(t,x)$ on $(a,0]$ and y is a solution of $\dot y=f(t,y)$ on $[0,b)$ and $x(0)=y(0)$ then :
$$\begin{align}
z(t)=% 1 cases
\begin{cases}
x(t) \text{ if } a\leq t<0\\
y(t) \text{ if } t>0
\end{cases}
\end{align}$$

## Existence and uniqueness
We need lipshitz continuity, A function g is lipshitz if if:
$$\begin{align}
|g(x)-g(y)|\leq L|x-y|
\end{align}$$
for any $x,y\in \R^n$,

A function g is called locally lipshitz continuous if its lipshitz continuous on every compact subset of $\R^n$

### The lipshitz constant
A function g is differentiable is called differentiable at a point $x_0$ if there is linear mapping $Dg(x_0):\R^n\rightarrow\R^n$ So that
$$\begin{align}
\limits_{x \rightarrow x_0}\frac{|g(x)-g(x_0)-Dg(x_0)(x-x_0)|}{|x-x_0|}=0
\end{align}$$
if $g\in C^1$ then $Dg(x_0)$ is the jacobian.

If this derivative is bounded, then the function must be lipshitz.

$Dg< C\implies$ lipshitz

$$\begin{align}
|g(y)-g(x)|=|\int_0^1 \frac{d}{ds}g(x+s(y-x))ds|\\
=|\int_0^1 Dg(x+s(y-x))(y-x)|\\
\leq \int_0^1|Dg(x+s(y-x))(y-x)|ds\\
\leq \int_0^1|Dg(x+s(y-x))| |y-x|\\
\leq \int_0^1\sup |Dg||y-x|
\end{align}$$
## Theorem (Uniqueness)
Suppose $f(t,x)$ is lipshitz continuous in $x$ with constant $L$ for all $t\geq 0$ then if $x$ and $y$ are solutions to $\dot x =f(t,x),\dot y = f(t,y), t>0$ then we have the following
estimate then $|x(t)-y(t)|\leq e^{Lt}|x_0-y_0|$

In particular if $x_0=y_0$ then $x(t)=y(t)$
