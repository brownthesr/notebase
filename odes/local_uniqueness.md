# Local Uniqueness

Remember we are interested in
$$\begin{align}
x(t)=x_0+\int_0^t f(s,x(s))ds
\end{align}$$
if f is continuous then this is equivalent to the IVP.

We first proved uniqueness under the assumption that f is globally lipshitz continuous

$$\begin{align}
e^{-Lt}|x_0-y_0|\leq |x(t)-y(t)|\leq e^{Lt}|x_0-y_0|
\end{align}$$

We also proved existence with the piccard-lindeloff theorem. (Global Version):

Suppose $f:\R\times \R^n\rightarrow \R^n$ satisfies $|f(t,x)-f(t,y)|\leq L|x-y|$ uniformly in t for all x,y in $\R^$. Then $\exists! C^1$ solution $x(t)KL$

We assumed global lipshitz, we only used this when showing it was a contraction. We can probably improve this, global is far too strong.

## Definition Local Lipshitz
Localizing existence and uniqueness

f is locally lipshitz if for every compact subset we can bound $|f(s,x)-f(s,y)|\leq L |x-y|$  for all $x,y\in K, s\in [-T,T]$

### Remark
lipshitz implies locally lipshitz, but not the other way around
### Example:
- $f(x)=x^2$
- Any $f(t,x)$ in the function space $C([0,t])$
## Theorem: Localizing uniqueness

suppose $f(t,x)$ is locally lipshitz and uniformly  in t then any two solutions of $\dot{x}=f(t,x),x(0)=x_0$ agree on their common time interval

proof:
suppose $x,y$ are two solutions to the IVP defined on the time interval $I_x,I_y$ respectively then let:
$$\begin{align}
I=\{t\in I_x\cap I_y, x(t)=y(t)\}
\end{align}$$
if I is both closed and open then either it is the entire set or empty. clearly it is not empty by the initial condition

I is closed because $x(t)-y(t)$ is continuous

We now show that it is open. To show E is open we must show there is an open interval around each time $t_0$ ($x(t_0)=y(t_0)$) then $x(t)=y(t)$ in an open interval $(t_0-\delta,t_0+\delta)$

WLOG assume $t_0=0$ take $r>0$ with $x(0), \overline {B_r(x_0)}\in U$ then by local lipshitz $\exists L>1$ where $f(t,x)$ is lipshitz continuous on this ball. Since f is continuous on the set $[-1,1]\times B$. Then it is bounded by $M$. set $t^*=\sup(t:x(t)\in \overline B)$. then:
$$\begin{align}
r=|x(t^\star)-x_0|\leq Mt^\star
\end{align}$$
So for all time before $t^\star$ then its in the ball and we can apply the lipshitz condition. and use the normal uniqueness

## Theorem Maximum interval of existence
if f is locally lipshitz. then it may have a finite time blow up. or it will blow up at at some point, whether it be infinite or finite.
