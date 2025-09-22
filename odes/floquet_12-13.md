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
Remark. if we could find a matrix B with $e^{Bt}=M$ then we could define a peridoic matrix:
$$\begin{align}
P(t)=\Phi(t)e^{-Bt}
\end{align}$$
This is T peridodic:
$$\begin{align}
P(t+T)=\Phi(t+T)e^{B(t+T)}=\Phi(t)MM^{-1}e^{-Bt}\\
=\Phi(t)e^{-Bt}
\end{align}$$
Then clearly:
$$\begin{align}
\Phi(t)=p(t)e^{Bt}
\end{align}$$
And we have proven it. But not for real entries
