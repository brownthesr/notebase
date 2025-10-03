# Floquet theory

Consider the problem:
$$\begin{align}
\dot{x}=A(t)x
\end{align}$$
where $A(t)$ is T periodic  

Remark $x(t)$ will not be periodic in general. Example $A(t)=a$ then the solution is $e^{at}$ which is definitely not periodic.

Question is $x(t)$ "close" to being periodic? If we remove the exponential then we get a periodic function.

$x(t)$ will be periodic if we allow some exponential factor

# Theorem Floquet
There is a matrix $B$ and a T periodic function $p(t)$ with $p(0)=I$ (possibly with complex entries), such that $\Phi(t)=p(t)e^{Bt}$

There is a matrix $C$ and a $2-T$ periodic function $\hat{p}(t), \hat{p}(0)=I$ (all real entries) such that:
$$\begin{align}
\Phi(t)= \hat{p}(t)e^{Ct}
\end{align}$$
Not super useful but very beautiful.
## Example (1 D)
For a scalar equation we have that
$$\begin{align}
\dot{x}(t)=a(t)x(t)
\end{align}$$
then the solution is $x(t)=e^{\int_0^ta(s)ds}x_0$. Define $\overline{a} = \int_0^Ta(s)ds$ and $p(t)=e^{\int_0^t(a(s)- \overline{a})ds}$. (This is $T-$periodic) then clearly:
$$\begin{align}
x(t)=p(t)e^{ \overline{a}t}x_0
\end{align}$$

## Definition: Monodromy Matrix
Let $\Phi(t)$ be the fundamental matrix solution note:
$$\begin{align}
\frac{d}{dt}\Phi(t+T)=A(t)\Phi(t+T)
\end{align}$$
So this is also a fundamental matrix
$$\begin{align}
M=\Phi(0)^{-1}\Phi(T)\\
\Phi(t+T)=\Phi(t)M
\end{align}$$
First note that M is invertible. Secondly note the previous equality

Proof: Apply lioville formula so the wronskian $d(\Phi(t))=\det(\phi(0))e^{\text{stuff}}$. If the determinant is nonzero then this is always nonzero so all of the things are invertible

## Theorem: Floquet (again)
 Floquet: There is a matrix B and a T periodic function $p(t),p(0)=I$ possibly with complex entries such that $\Phi(t)=p(t)e^{Bt}$

Furthermore there is a matrix X and a 2T periodic function $\tilde{p}$ both with real entries such that $\Phi(t)= \tilde{p}(t)e^{Ct}$

To prove the other thing about the monodromy matrix:
$$\begin{align}
\Phi(t+T)=\Phi(t)M
\end{align}$$
This follows by uniqueness of initial condition.

## Definition: Floquet multipliers
The floquet multipliers are the eigenvalues of the Monodromy matrix that could be repeated or complex.

Corresponding to each eigenvalue there is an eigenvector $\omega_j$ possibly complex.
## Define: Periodic (ish) solutions
Define the following solution trajectory starting at $\omega_j$
$$\begin{align}
\chi(t):=\Phi(t)\omega_j
\end{align}$$
First note that we have the following relationship:
$$\begin{align}
\chi(t+T)=\Phi(t+T)\omega_j=\Phi(t)M \omega_j=\lambda_j\chi_j(t)
\end{align}$$
This implies that $\chi(t+kT)=\mu_j^k\chi_j(t)$. Note this either diverges to infinity or converges to zero.

## Define floquet exponents
$$\begin{align}
\gamma_j=\frac{1}{T}\log(\mu_j)
\end{align}$$
for the complex logarithm $\log(z)=\log(|z|)+i \text{arg}(z)$

Remark if $\mu_j<0$ then $\gamma = \log|\mu_j|+i\pi$

## Factorization into an exponential and a periodic function
We have that $\chi_j(t)=e^{\gamma_j t}p_j(t)$. This is a proposal:
$$\begin{align}
p_j(t+T)=\chi_j(t+T)e^{-\gamma_j (t+T)}=\mu\chi_j(t)e^{-\gamma_j(t+T)}\\
=e^{\gamma T}\chi_j(t)e^{-\gamma(t+T)}=p_j(t+T)
\end{align}$$
So this p is periodic. Furthermore we just showed that we could factor $\chi_j$ into the exponential and periodic parts. So we have proved floquet for the eigenvectors. However these were all complex, lets go on to deal with real entries.

## Factorization into an exponential and a real periodic function.
Let $\chi_j(t)=e^{\frac{t}{T}\log(|\mu_j|)}q_j(t)$. This is different from before because now we have the absolute value:
$$\begin{align}
q_j(t+T)=\chi_j(t+T)e^{-\frac{t+T}{T}\log(|\mu_j|)}\\
=\chi_j(t)\mu_je^{-\frac{t}{T}\log(|\mu_j|)-\log(|\mu_j|)}\\
=\chi_j(t)e^{\log(\mu_j)}e^{-\frac{t}{T}\log(|\mu_j|)-\log(|\mu_j|)}\\
=\chi_j(t)e^{\log(|\mu_j|)+i\theta}e^{-\frac{t}{T}\log(|\mu_j|)-\log(|\mu_j|)}\\
=\chi_j(t)e^{i\theta}e^{-\frac{t}{T}\log(|\mu_j|)}\\
\end{align}$$
note chi could be complex but he said to ignore that for now because it will cancel out later. This also doesn't quite work but he says it will work out. if this is real then this works for a period of 2T because the angle will just be -1 so two of them will be 1.

## Matrix computation (Floquet Theorem)
The monodromy matrix is $\Phi^{-1}(0)\Phi(T)$ and $\Phi(t+T)=\Phi(t)M$ by uniqueness. This implies that :
$$\begin{align}
\Phi(t+kT)=\Phi(t)M^k
\end{align}$$
Remark. if we could find a matrix B with $e^{Bt}=M$ then we could define a periodic matrix:
$$\begin{align}
P(t)=\Phi(t)e^{-Bt}
\end{align}$$
This is T periodic:
$$\begin{align}
P(t+T)=\Phi(t+T)e^{B(t+T)}=\Phi(t)MM^{-1}e^{-Bt}\\
=\Phi(t)e^{-Bt}
\end{align}$$
Then clearly:
$$\begin{align}
\Phi(t)=p(t)e^{Bt}
\end{align}$$
And we have proven it. But not for real entries

## Note
We do the eigenvectors first just to provide context.

- We have been able to write $\Phi(t)=p(t)e^{Bt}$. To study the stability we only need to study the stability of this B matrix. This is the first scenario for complex entries

- In the second case (for real entries)

Last time we proved that if $\pi(t,s)\leq Ce^{\alpha(t-s)}$ then we have stability. This obviously holds here I think (continuity, any periodic function that is continuous is bounded)

1. Floquet multiplies are the eigenvalues of the monodromy matrix $\mu_j$ with the eigenvectors $w_j$ which are possibly complex
2. Define $\chi(t)\Phi(t)w_j$. In this case we know that $\chi_j(t)$ is kind of periodic
3. Floquet exponential $\gamma_j=\frac{1}{T}\log(\mu_j)$- for the general logarithm
    - We were then able to factorize this dude into exponential and periodic functions. $\chi_j(t)=e^{\gamma_jt}p_j(t)$ where $p_j$ is periodic.
4. If all of the floquet multipliers (and their eigenvectors) are real then it can be factored into an exponential and a real periodic function of $2T$

From all this we would like to factor $\Phi(t)$ into an exponential and periodic function
## RETURN TO THE MATRIX:
Recall that $\Phi(t+kT)=\Phi(t+(k-1)T)M=\dots=\Phi(t)$
### Remark
if we can find a matrix B with $e^{Bt}=M$ then define $p(t)=\Phi(t)e^{-Bt}$

This implies that $\Phi(t)=p(t)e^{Bt}$. We just need to find the matrix exponential

## Log of a Matrix!
Goal given a matrix $A$ we want to find $B$ such that $e^B=A$ that is $B=\log(A)$. Assume that A is invertible since all matrix exponentials are invertible.

Result: if the matrix $A$ has real entries and all of its real eigenvalues have positive real part then there exists $\log(A)$ whose entries are all real (Note this is satisfied by our matrix exponential)

Step one: decompose the matrix into jordan canonical form let:
$$\begin{align}
J=Q^{-1}AQ
\end{align}$$
be the jordan canonical form. Suppose we know $\log(J)$ then $\log(A)=Q\log(J)Q^{-1}$ note:
$$\begin{align}
e^{\log(A)}=e^{Q\log(J)Q^{-1}}=Qe^{\log(J)}Q^{-1}=QJQ^{-1}=A
\end{align}$$

Step two: Define $\log(J)$

Note that because J is a jordan canonical form then $J=\text{diag}(J_1,\dots,J_n)$. Where each $J_i$ is a jordan block. Suppose $\log(J_i)$ is well defined then:
$$\begin{align}
\log(J)=\text{diag}(\log(J_1),\dots,\log(J_n))
\end{align}$$
To verify this note that $\text{diag}(A,\dots,B)^k=\text{diag}(A^k,\dots,B^k)$
$$\begin{align}
e^{\log(J)}=e^{\text{diag}(\log(J_1),\dots,\log(J_n))}\\
=\sum_{k=0}^\infty \frac{1}{k!}(\text{diag}(\log(J_1)^k,\dots,\log(J_n)^k))\\
=\text{diag}(e^{\log(J_1)},\dots,e^{\log(J_n)})\\
=\text{diag}(J_1,\dots,J_n)
\end{align}$$
Since we assumed that $\log(J_i)$ is well defined.

Step three: define $\log(J)$ (a Jordan Block) with all real eigenvalues. Consider a single $k\times k$ jordan block with real positive eigenvalue $\lambda$.
$$\begin{align}
J=\Lambda I+N\\
=\Lambda(I+\Lambda^{-1}N)
\end{align}$$
We define the log to be
$$\begin{align}
\log(J)=\log(\lambda)I+\sum\limits_{k=1}^{n-1}\left(\frac{(-1)^j}{j\lambda^j}N^j\right)
\end{align}$$
You can check that $e^{\log(J)}=J$. This is the solution.

Another situation is if we have the standard $2\times 2$ jordan block for complex eigenvalues. $J=\text{diag}(D,\dots,D)+N$ where D is the complex block.

Let $\overline{D}=\text{diag}(D,\dots,D)$ then $J=\overline{D}(I+D^{-1}N)$. We then define
$$\begin{align}
\log(J)=\text{diag}(\log(D),\dots,\log(D)) + \sum\limits_{j=1}^{n-1}\left(\frac{(-1)^k}{j}D^{-j}N^j\right)
\end{align}$$
The matrix log is $\rho+i\omega = re^{i\theta}$ then the matrix log of d is $\log(D)=\log(r)I+[[0,-\theta],[\theta, 0]]$

## Stability of periodic system
suppose we have the fundamental solution $\Phi(t)$ with monodromy matrix $M=\Phi(0)^{-1}(0)\Phi(T)$. This is invertible with $\Phi(t+T)=\Phi(t)M$

we then have the floquet multipliers as the eigenvalues of $M$ the monodromy matrix $\mu_1,\dots,\mu_n$ with corresponding eigenvectors $w_j$. We also take the floquet exponential $\gamma_j=\frac{1}{T}\log(\mu_j)$ (the complex logarithm). The floquet exponentials and multipliers will tell us about the stability.

Earlier we proved the result:
$$\begin{align}
\chi_j(t)=\Phi(t)\omega_j=e^{\gamma_jt}p_j(t)
\end{align}$$
where $p_j(t)$ is T-periodic.

if $\mu_j$ are all real then we have the $\chi_j(t)=e^{\frac{t}{T}\log|\mu_j|}q_j(t)$. where $q_j$ is 2T periodic.

### Corollary
we have
1. if all floquet exponentials have negative real part $\gamma_j<0$ (all floquet multipliers have $||\mu_j||<1$) then there is an M and $\alpha>0$ such that:
$$\begin{align}
|\Phi(t)x_0|\leq Me^{-\alpha t}
\end{align}$$
then 0 is asymptotically stable.

If all floquet multipliers have $|\mu_j|\leq 0$ (The real part of the exponentials are less than or equal to zero). and the multipliers with $|\mu_j|=1$ have a non-degenerate eigenspace then the system is stable:
$$\begin{align}
|\Phi(t)x_0|\text{ is bounded}
\end{align}$$

## Trick for showing instability
<!-- NOTE: Use this!! -->
$\det(M)=\frac{\det(\Phi(T)}{\det(\Phi(0))}=e^{\int_0^T\\text{tr}(A(s))}ds$ by the lioville formula.

this means that
$$\begin{align}
\prod_{j=1}^n\mu_j=e^{\sum T\gamma_j}=e^{\int_0^T\text{tr}(A(s))}
\end{align}$$
This implies that the real part of $\sum_j T\gamma_j=\int_0^T \text{tr}(A(x))ds$.

We then know that if $\frac{1}{T}\int_0^T tr(A(s))ds>0$ then there is at least one $\gamma_j>0$. This means that the system is unstable.

## Hills equation
$$\begin{align}
\ddot{x}+q(t)x=0
\end{align}$$
$q(t)$ is T periodic.

$$\begin{align}
% 2 x 2 BMatrix
\begin{bmatrix}
0 & 1 \\
-q(t) & 0
\end{bmatrix}
\end{align}$$
This is the A. We can choose $\Phi(0)=I$. in this case:
$$\begin{align}
M=\Phi(0)^{-1}\Phi(T)=\Phi(T)
\end{align}$$
we the know that:
$$\begin{align}
\det(M)=\det(\Phi(t))=1
\end{align}$$
since the trace is zero

so we know that $\mu_1\mu_2=1$ this gives us the characteristic equation of M is
$$\begin{align}
\mu^2-2\Delta \mu+1=0
\end{align}$$
where $\Delta=tr M$.

We just need to look at trace of $M$.

Write out using the quadratic formula:
$$\begin{align}
\frac{2\Delta \pm \sqrt{\Delta^2-1}}{2}
\end{align}$$
if $\Delta^2>0$ then both eigenvalues are real and have the same sign. So one of them will have magnitude greater than one. So the system is unstable.

There are two linearly independent solutions of the form:
$$\begin{align}
\chi_{\pm}(t)=e^{\frac{1}{T}\log|\mu_\pm|t}p_\pm(t)
\end{align}$$
where $P$ is 2 T periodic. Then the stable is unstable.

if $\delta^2<1$ then we have imaginary eigenvalues and the magnitude will always have absolute value equal to one. So we have a stable solution.
$$\begin{align}
\mu_\pm=\Delta\pm i\sqrt{1-\Delta^2}
\end{align}$$
both eigenvalues have modulus 1.

We have two linearly independent solutions:
$$\begin{align}
\chi_\pm (t)=e^{\frac{1}{T}i\arg(\mu_{\pm})t}p_\pm(t)
\end{align}$$
So clearly this system is bounded. but not necessarily asymptotically stable

Last case if $\Delta^2=1$ then there is a single real eigenvalue: (it has to be 1 or -1)
$$\begin{align}
\mu=\Delta
\end{align}$$
if there are two solutions
$$\begin{align}
p_\pm(t\pm T)=\sigma p_{\pm}(t)
\end{align}$$
The system is stable

or if the multiplier is degenerate then the two solutions are $p_+(t)$ and $p_+(t)+tp_-(t)$

Thm hills equation is stable if $|\Delta|<1$ and unstable if $|\Delta|>1$

## Question
Consider
$$\begin{align}
\dot x = A(t)x+b(t)
\end{align}$$
where both are $T$ periodic. Does the System have a $T$ periodic solution.
## Theorem
If $1$ is not an floquet multiplier for the homogeneous system then there is a $T$ periodic solution

proof if $x(T)=x(0)$ then it is T periodic.

but by Duhamels formula we have that:
$$\begin{align}
x(T)=\Phi(T)x(0)+\int_0^T\Phi(T)\Phi^{-1}(s)b(s)ds\\
(I-\Phi(T))x(T)=\int_0^T\Phi(T)\Phi^{-1}(s)b(s)ds
\end{align}$$
This is invertible if 1 is not an eigenvalue
