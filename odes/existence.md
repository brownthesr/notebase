# Existence

## Definition

For a subset X of a normed vector space V a map $\phi$ is called a strictv contraction if :
$$\begin{align}
||\phi(x)-\phi(y)|| \leq \mu ||x-y||
\end{align}$$
where $\mu<1$

## Theorem Contraction Mapping theorem
If X is a closed subset of a complete normed space V and $\phi: X\rightarrow X$ is a strict contraction, then there exists a unique fixed point

Proof:

construct a sequence $x_{n+1}=\phi(x_n)$ take:
$$\begin{align}
||x_{n+1}-x_n||=||\phi(x_n)-\phi(x_{n-1})||\leq \mu ||x_n-x_{n-1}||\\
\leq \mu^{n}||\phi(x_0)-x_0||\\
||x_n-x_m||\leq \sum_{j=m}^{n-1}||x_{j+1}-x_j||\\
\leq \sum\limits_{j=m}^{n-1}\left(\mu^j||\phi(x_0)-x_0||\right)\\
\leq ||x_1-x_0||\frac{\mu^m}{1-\mu}
\end{align}$$
Thus clealy $x_m$ is a cauchy sequence. So it converges to something in the space.

<!-- NOTE: Remark we can pass limits inside continuous functions -->
The contractiotn mapping theorem is a comman tool for proving existence.
<!-- NOTE: Gronwalls says that: -->
$$\begin{align}
e^{-LT}|x_0-y_0|\leq |x(t)-y(t)|\leq e^{LT}|x_0-y_0|
\end{align}$$
<!-- NOTE: What are the assumptions on Gronwalls? -->
## Picard lindelof Theorem Global Existence.

If f is globally lipshitz uniformly in t then there is a unique solution of the integral form.

steps:
- Local Existence
- Global Extension

### Local Existence Proof
First, we define
$$\begin{align}
X=\{x\in C[0,T], x(0)=x_0\}
\end{align}$$
This is a closed subset of the banach space $C([0,T]\rightarrow \R^n)$

Define the mapping:
$$\begin{align}
\Phi[x](t)=x_0+\int_0^tf(s,x(s))ds \text{ for } t\in[0,T]
\end{align}$$

$$\begin{align}
x_0+\int_0^t a(x_0+\int_0^)
\end{align}$$
