# Completed Metric Space

We Can complete a space and identify a subset of the completed space that has an isometry with the original space
<!-- TODO: Re-read me later, write me down-->
<!-- FIXME: In the proof of the completed space, How can a sequence be cauchy if it is constant? Isn't that mute? -->

## Banach Fixed Point theorem

if T is a contraction on X them T has a unique fixed point (X is nonempty and complete metric space)

Proof:
$$\begin{align}
d(x_{m+1},x_m)=d(Tx_m,Tx_{m-1})
\leq \alpha d(x_m,x_{m-1})
\dots
\leq \alpha^m d(x_1,x_{0})
\end{align}$$
then:
$$\begin{align}
d(x_m,x_n)\leq d(x_m,x_{m+1})+\dots+ x+d(x_{n-1},x_n)\\
\leq (\alpha^{m}+\alpha_{m+1}+\dots +\alpha_{n-1})d(x_{1},x_0)\\
\leq (\frac{\alpha^m-\alpha^n}{1-\alpha})d(x_{1},x_0)\\
\leq (\frac{\alpha^m}{1-\alpha})d(x_{1},x_0)
\end{align}$$

This can be made arbitrarily small given that m is sufficiently large. This $x_m$ is cauchy thus it converges by completeness.

## Claim
x is a fixed point

$$\begin{align}
0\leq d(Tx,x)\leq d(Tx,x_n)+d(x_n,x)
\leq d(Tx,Tx_{n-1})+d(x_n,x)
\leq \alpha d(x,x_{n-1})+d(x_n,x)
\end{align}$$
Both of these terms go to zero. Thus this is a fixed point.

Claim x is a unique fixed point. Assume BWOC that there were two
$$\begin{align}
d(x,y)=d(Tx,Ty)\leq \alpha d(x,y)
\end{align}$$
Thus $d(x,y)=0$ so $x=y$
## Corollaries
- $d(x_m,x)\leq \frac{\alpha^m}{1-\alpha}d(x_0,x_1)$ a prior estimate of convergence (very pessimistic).
- $d(x_m,x)\leq \frac{\alpha}{1-\alpha} d(x_{m-1},x_m)$. This gives us a stopping criterion.
## Theorem Contraction on a ball
Let $T:X\rightarrow X$ complete metric space. Let $T$ be a contraction on the closed ball $\overline{B}(x_0,r)= \{x|d(x_0,x)\leq r$

this means that $\exists \alpha \in (0,1)$ such that $\forall x,y\in \overline{B}(x_0,r): d(Tx,Ty)\leq d(x,y)$

Thm assume that $d(x_0,Tx_0)\leq (1-\alpha)r$ then then the iteration converges to some fixed point $x\in \overline{B}(x_0,r)$ and the fixed point is the unique fixed point in the ball

Proof: From the proof of the fixed point theorem we get that:
$$\begin{align}
d(x_0,x_m)\leq \frac{1}{1-\alpha}d(x_0,x_1)\leq r
\end{align}$$
thus $x_m\in \overline{B}(x_0,r)$. The limit then also belongs to the ball because the ball is closed. What we proved here is not that it converges, but just that every other iterate is also in the ball. We proved that it converges somewhere else.

This is also a method to solve linear systems.
## 5.3 Picard Theorem for ODEs

$$\begin{align}
x'=f(x,t)\\
x(t_0)=x_0
\end{align}$$
goal use the BFP to give conditions under which ivp has a unique solution.

Thm: Let f be continuous on a rectanular region:
$$\begin{align}
R=\{(t,x): |t-t_0|\leq a,|x-x_0|\leq b\}
\end{align}$$
Basically a rectangle of side lengths $2b,2a$. From this we know that f is bounded (continuous on a compact set). We can then find a c positive:
$$\begin{align}
|f(t,x)|\leq c
\end{align}$$
on this region.

We also assume that f is lipshitz continuous in x only.
