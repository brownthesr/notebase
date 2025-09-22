# First Order Autonomous equations

## Example one

$$\begin{align}
\dot x = f(x),x(0)=x_0\\
\end{align}$$
we can solve this by separation of variables:
$$\begin{align}
\frac{\dot x}{f(x)}=1\\
\end{align}$$
integrating both sides from $t_0=0,t$
$$\begin{align}
\int\limits_{0}^{t}\frac{\dot x(s)ds}{f(x(s))}= t\\
\int\limits_{x_0}^{x(t)}\frac{ du}{f(u)}= t\\
\end{align}$$
The reason that we are allowed to make that substitution is because of usubstituion

So we can set that integral equal to a function:
$$\begin{align}
F(x)=\int\limits_{x_0}^{x(t)}\frac{ du}{f(u)}\\
\end{align}$$

So any solution must satisfy $F(x(t))=t$ or $x(t)=F^{-1}(t)$. From here we want to understand $F^{-1}$. knowing its range and domain will give us the domain and range of x.

Earlier we made the assumption that $f(x_0)\neq 0$. so it is not zero in some neighborhood. Assume that it is negative. Let $(x_1,x_2)$ be the largest interval over which this function is negative.

We then know that $\limits_{x \rightarrow x_2}F(x)=T_1 \leq 0$ $\limits_{x \rightarrow x_2}F(x)=T_2 \geq 0$. thus the range of $F(x)$ is $(T_1,T_2)$ and the domain is $(x_1,x_2)$.

From this we know that the range of $F^{-1}$ is $x_1,x_2$ and the domain is to these Ts. So we can have the solution be defined for all t if these integerals are infiniteok.

## Transformations
Note that we can often transform equations bty using an appropriate change of variables. When you do this take a new variable $y=f(x,t)$ and then just differentiate through this using the chain rule
$$\begin{align}
\dot y = f_x \dot{x}+f_t
\end{align}$$
Some nice transformations you can use are $y=\frac{x}{t}$ (Homogenous) $y=x^{1-n}$ (for bernoulli).

For example take $\dot x = -x +x^3$. From here make the transformation $y=x^{1-3}=x^{-2},$ then $\dot y = -2 \frac{1}{x^3}\dot x=-2 \frac{1}{x^3}(-x+x^3)=2y-1$
