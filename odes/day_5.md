# Solution trajectory

## Def

An ode
$$\begin{align}
\dot{x} = f(t,x)
\end{align}$$
Is called autonomous if $f(t,x)$ does not depend on t

We can always turn a non-autonomous ode to an autonomous ode by adding another variable:
$$\begin{align}
\dot{t} = 1
\end{align}$$

We defined the trajectory of the solution
## Definition
The trajectory of an autonomous ode is the image of a solution as a subset of $\R^n$ that is if $\dot{x}=f(x)$ on a time interval $I$, then $\Gamma_x=x(I)$ is the trajectory.

## Remark
Trajectories of non-autonomous ODE are subsets of $(-\infty,\infty)\times \R^n$.

## Lemma: Trajectories of different initial conditions do not cross.

Suppose that $f(t,x)$ is lipshitz continuous for all time t in x. If $\Gamma_1,\Gamma_2$ are trajectories of $\dot{x}=f(x)$, then we have the following conclusion:

Either they are disjoint or $\Gamma_1\cup \Gamma_2$ (Basically you could have them going over different intervals)

pf:

Suppose there is a point $z_0\in \Gamm_x\cap\Gamma_y$. then $\exists t_x\in I_x,t_y\in I_y$ So that $x(t_x)=z_0,y(t_y)=z_0$ then define $\overline{x} = x(t+t_x), \overline{y}=y(t+t_y)$ then we know that

$$\begin{align}
\overline{\dot{x}} = f( \overline{x})\\
\overline{\dot{y}} = f( \overline{y})\\
\overline{x}(0)=z_0= \overline{y}(0)=z_0
\end{align}$$

Thus we know that $ \overline{x} = \overline{y}$

Let:
$$\begin{align}
z(t)=% 2 cases
\begin{cases}
\overline{x} \text{ if } x\in I_x\\
\overline{y} \text{ if } t\in I_y
\end{cases}
\end{align}$$
So if there is in intersection we proved that the union is also a solution.

## Phase Line Analysis
Consider the first order autonomous ode
$$\begin{align}
\dot{x} = f(x)\\
x(0)=x_0
\end{align}$$
## Lemma
if $f$ is lipshitz, and $f> 0$ on $(a,b)$ and $f(a)=f(b)=0$ then for any $x_0\in (a,b)$ we have
$$\begin{align}
\limits_{t \rightarrow -\infty}x(t)=a\\
\limits_{t \rightarrow \infty}x(t)=b
\end{align}$$

To prove this. Note that if the solution is ever a or b, then it will always stay at one of those, so by the previous lemma since they can't intersect. So for $x_0\in (a,b)$ the solution never reaches either of those.

pf:
since $x(t)$ is continuous and $x_0\in (a,b)$ the entire solution must live in the interval by the IVT. this implies that $ \dot{x} =f(x(t))>0$. thus $x$ is strictly monotonic. Therefore $\limits_{t \rightarrow \pm \infty}$ both exist. We want to show that this limit is $a,b$.

suppose BWOC that $x(t)\leq c < b$ for $t> 0$, then $\inf_{t>0} f(x(t))\geq \inf_{[x_0,c]} f(x)=  \mu>0$ where mu is the lower bound that the continuous function f acheives.

Then $b\geq x(t)=x_0+\int\limits_{0}^{t}f(x(s))ds\geq x_0+\mu t$. That means that $b\geq \infty$. This is a contradiction. The contradiction here comes from the fact that we were able to find a $\mu>0$. If $c=b$ then the infimum is definitely 0 and this contradiction does not work.

## Definition
Normed space given a vector space $V$ over $\R$ or $\C$, we say that $||\odot||:V\rightarrow \R$
is a norm on $V$ and call it a normed vector space if we have positivity, scaling, and the triangle inequality.

### Examples
Euclidean norm obviously

The space of linear operators
$$\begin{align}
||T||_{L}=\sup_{x\neq 0} \frac{|Tv|}{|v|}
\end{align}$$

The space of continuous functions with norm $\sup |f(x)|$

## Definition
Banach Space, A normed space that is complete.
