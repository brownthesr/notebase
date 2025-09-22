# Floating point arithmetic and computer algorithms

Numbers in base 10:
$$\begin{align}
34.1503=3*10+4*1+1*.1+5*.02+3*.0001
\end{align}$$
- Everything before the decimal is the integer part (34)
- 1503 is the fractional part.
- These two parts are separated by the radix
- base 10 is understood by context
- We typically can choose the base, Note that the maximum digit must be strictly smaller than the base.

Computers typically use base 2. Each digit is called a bit. 8 bits is a byte.

## Fixed point vs floating point
in fixed point we have a fixed radix point so we can write:
$$\begin{align}
1010.0010011101
\end{align}$$
The issue that we have with this is the artificial truncation.

Floating point representations allow the radix to move. We move the radix and add an exponent. So the integer and fractional parts are combined

- the significand is the integer and fractional part
- The exponent is where the radix goes
- The trailing bit tells us if it is plus or minus.

In single precision the first bit is the sign, the next 8 is the exponent, and the last 23 are the significand.

## Machine precision
Machine epsilon is the **relative** rounding error so its nicer to use:
$$\begin{align}
|\frac{x-fl(x)}{x}|
\end{align}$$
So the relative error metric. We will say that $\epsilon_{\text{machine}}$ is the maximum value of this number over all numbers. Roughly speaking is is the largest $\epsilon$ where $1+\epsilon=1$

The error is essentially $\text{base}^{\text{ number of significant digits}}$

## Round off and computing
- $\sqrt{1+x^4}-1$ for small positive x. Take the Taylor series.
- $e^x,x<0$. Take the Taylor series. This turns out to be bad because we are taking large negative numbers adding to large negative numbers. We lose small numbers as a result
- Computing the derivatives.

## Sensitivity
- Goal: understand sensitivity of numerical algorithms to round off errors (stability)
- understand sensitivity of solution to mathematical problems (conditioning)

### Example
$$\begin{align}
f(x)=\alpha x
\end{align}$$
how wiggling x impacts the output depends on $\alpha$.

### Perturbations
A measure of sensitivity is perturbation based:
$$\begin{align}
\hat{\kappa}(x)=\lim_{\delta \rightarrow 0}\sup_{||\delta x||\leq \delta}\frac{||f(x+\delta x)-f(x)||}{||\delta x||}
\end{align}$$
Which is the absolute condition number. This has nothing to do with algorithms so far. This is just a function.

We want the relative condition number:
$$\begin{align}
\kappa_f(x)=\frac{\frac{ ||\delta f||}{ ||f||}}{\frac{ ||\delta x||}{ ||x||}}
\end{align}$$
With norms and limits of course

If this number is small it is well conditioned, if it is large then it is ill conditioned. But it behaves like we would like it to:
$$\begin{align}
\frac{||\delta f||}{||f||}\leq \kappa_f(x)\frac{||\delta x||}{||x||}
\end{align}$$
Unsurprisingly if f is smooth then the condition numbers are just jacobians:
$$\begin{align}
\hat{\kappa}_f(x)=||J(x)||\\
\kappa_f(x)=\frac{||J(x)||||x||}{||f(x)||}
\end{align}$$
Generally just compute the jacobian. The hard part is that we have intuition for absolute condition numbers, but not necessarily for relative condition numbers.

Take the earlier example $f(x)=\alpha x, \hat{\kappa}=|a|,\kappa=\frac{|a||x|}{|ax|}=1$

### More examples
So this has a relative condition number of 1. So if we have a relative wiggle of size $\epsilon$ in x then we should see a relative wiggle of size $\epsilon$ in $f$.

What about  about $x^p,p>0$
$$\begin{align}
\hat{\kappa}=p|x^{p-1}|\\
\kappa = \frac{p|x^{p-1}||x|}{|x^p|}=p
\end{align}$$
so when $p>>1$ it is worse conditioned compared to $p<<1$. So if I make a mistake of $\epsilon$ in x then we will get a mistake of $p\epsilon$ in f

How about $f(x)=Ax$:
$$\begin{align}
\hat{\kappa}=||A||\\
\kappa = \frac{||A|| ||x||}{||Ax||}\leq ||A||||A^{-1}||
\end{align}$$
So for $l^2$ norms then this relative condition number is bounded above by this. This is achieve when $x$ hits the lowest singular value of $A$. If A is not invertible then it has a kernel and we could get infinity haha.

By a similar argument $f(x)=A^{-1}b$ has relative condition number bounded above by $||A||||A^{-1}||$.

## Definition: Condition number of a matrix:
$$\begin{align}
\kappa(A)=||A||||A^{-1}||
\end{align}$$
if using $l^2$ norms then $\kappa(A)=\frac{\sigma_1}{\sigma_m}\geq 1$ this is because $1=||I||=||A^{-1}A||\leq ||A^{-1}||||A||$
## Numerical Algorithms
We wish to understand how round off errors affect evaluation of f. This should depend on lack of accuracy due to precision and the conditioning of f.

### Examples
$f(x)=1+x, \tilde{f}(x)= \text{fl}(1)\oplus+ \text{fl}(x)j$

Fun fact the condition number of computing the condition number of a function is the condition number of a function.

## What we want: Forward Error
$$\begin{align}
\frac{||f(x)- \tilde{f}(x)||}{||f(x)||}=O(\epsilon_\text{Machine}).
\end{align}$$
One would hope that this would be related to the condition of f. This is the Forward error.

note that:
$$\begin{align}
FE(x)=\frac{|| \tilde{f}(x)-f( \tilde{x})||}{||f(x)||}+\frac{||f(x)-f( \tilde{x})||}{||f(x)||}
\end{align}$$
The idea is that we know how to wiggle x. So this (specifically the second one) is easier to deal with.

We know from before that:
$$\begin{align}
\frac{||f(x)-f( \tilde{x})||}{||f(x)||}\leq \frac{\kappa_f(x) ||x- \tilde{x}||}{||x||}
\end{align}$$
So this error is dependent on the condition number and the floating point truncation.

We want both of the things on the right to be about the same in magnitude. So they balance each other out. This motivates the definition:
## Definition backward error:
we say an algorithm is forward stable if:
$$\begin{align}
\frac{|| \tilde{f}(x)-f( \tilde{x})||}{||f(x)||}\leq \kappa(x)\frac{|| x- \tilde{x}||}{||x||}
\end{align}$$
The intuition behind this is that we want our triangle inequality to balance out.

A forward stable algorithm provides almost the right answer to a closely related question.

Our forward stable algorithm guarantees that $FE(x)\lesssim \kappa(x)\epsilon_{ \text{machine}}$. This is the best we can hope for. This is called forward error analysis. It is frequently technical and difficult.

## Definition backward stable:
We say an algorithm is backward stable if:
$$\begin{align}
\tilde{f}(x)=f( \tilde{x})\\
||x- \tilde{x}||=||x||O(\epsilon)
\end{align}$$
This is even nicer than forward stability, because we just kill the first term.

The backward error can then be defined as:
$$\begin{align}
BE(x)=\inf\{\frac{||x- \tilde{x}||}{||x||}| \tilde{f}(x)=f( \tilde{x})\}
\end{align}$$
We won't use this.

Estimating error with backwards stable algorithms is frequently easier to show, but forward stable algorithms do not need to be backwards stable. (even though the converse is true).

## Axioms of floating point
for each $x, fl(x)=x(1+\epsilon)$ similarly for all operations $x\odot y=(x\cdot y)(1+\epsilon)$

Is floating point subtraction backwards stable?:
$$\begin{align}
(x(1+\epsilon_1)+y(1+\epsilon_2))(1+\epsilon_3)\\
=x(1+\epsilon_1)(1+\epsilon_3)-y(\text{same})
\end{align}$$
So the first is $\tilde{x}$ and the second is $\tilde{y}$ we then plug those into the other thing in the backward error.

is $1+x$ backwards stable?
$$\begin{align}
(1+(x)(1+\epsilon))(1+\epsilon_2)\\
=1(1+\epsilon_2)+x(1+\epsilon_1)(1+\epsilon_2)
=1+x((1+\epsilon_1)(1+\epsilon_2)+\frac{\epsilon_2}{x})
\end{align}$$
We want this to be $1+ \tilde{x}$. This cannot happen. Because we have an x in the denominator, this the x will explode for small x.
<!-- NOTE: Floating point will not be on the midterm, but there will be one question on conditioning. -->
The difference between this exercise and the last is that we could wiggle y. In this case we cannot wiggle one. Note that this is a forward stable algorithm.

The inner product operation is backwards stable. The outer product is not backwards stable. Intuition when you perturb a rank one matrix it is not rank one. It is definitely forward stable.

## Punch lines:
Well conditioned functions and stable implementations yield reliable accuracy.

## Eigenvalue Conditioning
Is the operation that takes a matrix and outputs the eigenvalue well conditioned

If $A$ is diagonalizable then the absolute condition number of computing the eigenvalues is $\kappa(V)$ The condition number of the matrix. So if the eigenvectors are close to linearly dependent then bad things will happen and the condition number will be huge. We will prove this soon.
### Example
$$\begin{align}
A = % 2 x 2 BMatrix
\begin{bmatrix}
1 & 1 \\
0 & 1+\epsilon
\end{bmatrix}
\end{align}$$
the eigenvectors get closer and closer to linearly dependent. $(1-\lambda)(1+\epsilon-\lambda)=\lambda^2-(2+\epsilon)\lambda+(1+\epsilon)=0, \lambda = \frac{(2+\epsilon)\pm \sqrt{(1+\epsilon)^2-4(1+\epsilon)}}{2}$

Note if the matrix is normal. Then the norm of this matrix is literally 1 and awesome.

Computing eigenvalues via the zeros of the determinant is not well conditioned.
