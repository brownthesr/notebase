# Project TODO / FIXME / NOTE Summary

## .

- **TODOs.md:1** — `# Project TODO / FIXME / NOTE Summary`
- **TODOs.md:5** — `- **note_creator.py:7** — `TAGS = ["TODO", "FIXME", "NOTE"]``
- **TODOs.md:6** — `- **note_creator.py:30** — `md.write("# Project TODO / FIXME / NOTE Summary\n\n")``
- **TODOs.md:10** — `- **functional_analysis/3.1.md:27** — `<!-- NOTE: This will be on the exam -->``
- **TODOs.md:11** — `- **functional_analysis/3.1.md:140** — `note that $2|(y_n+y_m)/2-x|\geq 2d(x,M)$``
- **TODOs.md:12** — `- **functional_analysis/3.1.md:181** — `then note that $Y^\perp = \text{span}(Y)^\perp, Y^\perp$ is also closed``
- **TODOs.md:13** — `- **functional_analysis/3.1.md:192** — `<!-- NOTE: This may be on the exam -->``
- **TODOs.md:14** — `- **functional_analysis/3.1.md:202** — `in the other direction assume that the perp is zero. note then that we can write anything as the closure of the span of M and its perp. Since the perp  is zero $x=y$ so we can write anything as something in the closure of the span. So they are equal``
- **TODOs.md:15** — `- **functional_analysis/day_4.md:4** — `<!-- TODO: Re-read me later, write me down-->``
- **TODOs.md:16** — `- **functional_analysis/day_4.md:5** — `<!-- FIXME: In the proof of the completed space, How can a sequence be cauchy if it is constant? Isn't that mute? -->``
- **TODOs.md:17** — `- **functional_analysis/HW3.tex:62** — `Take some arbitrary cauchy sequence. Note that you can write it via telescoping as:``
- **TODOs.md:18** — `- **functional_analysis/HW3.tex:102** — `From here note that we can always choose $n$ large enough so that the first term is less than $\epsilon/2$ this just follows from the definition of the shauder basis.``
- **TODOs.md:19** — `- **functional_analysis/HW3.tex:111** — `So we can get arbitrarily close to anything in x with a thing from P. Now note that P is countable. This follows from the fact that $Q$ is countable and we are only taking finite sums over the countable shauder basis.``
- **TODOs.md:20** — `- **functional_analysis/HW3.tex:118** — `To do this note first that by problem 5 the operator defined by $y=(\eta_j)$ where $y=Tx,\eta_j=\xi_j/j,x=\xi_j$ is linear and bounded in other words if:``
- **TODOs.md:21** — `- **functional_analysis/HW3.tex:125** — `To do this note that if $y\in R(T)$ then there is an $x$ such that $y_j=\frac{x_j}{j}$ furthermore we know that $x_j$ is in $l^\infty$ so $\max_j x_j=\max_jy_j j<\infty$``
- **TODOs.md:22** — `- **functional_analysis/HW3.tex:144** — `Choose $K>M, K\in \Z$. from here take the vector $y=(1,\dots,1,0,\dots)$ where the ones take up $K$ positions. Note that $y\in R(T)$ just take $x=(1,2,\dots, K,0,\dots)$ clearly $x\in l^\infty$ so that $Tx=y$.``
- **TODOs.md:23** — `- **functional_analysis/HW3.tex:146** — `from here note that $T^{-1}y=x$ from what we just showed and that $\max_j |x_j|=K$ however that means that:``
- **TODOs.md:24** — `- **functional_analysis/HW3.tex:150** — `Furthermore note that $y$ is unit norm so:``
- **TODOs.md:25** — `- **functional_analysis/HW3.tex:160** — `So the idea for this problem is that we actually need to create a basis. Choose the basis for x so that we have a basis $\{z_1,\dots z_k\}$ for Z and a separate basis for $X-Z$ $b_{k+1},\dots b_n$ (Note that both of these are nonepty by the fact that this is a proper subspace). Choose $b_{k+1}=x_0$ (we are allowed to do this since we can just pull other linearly independent vectors in). First notice that this is a bsis for the whole space because any thing in X is either in Z or not in Z ($X=(X\cap Z^c)\cup (X\cap Z)$). From here define the linear functional by:``
- **TODOs.md:26** — `- **functional_analysis/HW3.tex:191** — `now note that $0\in N(f), f(0)=0*f(0)=0$ so that $d(x,Y)\leq d(x,\{0\})=||x||$ thus:``
- **TODOs.md:27** — `- **functional_analysis/HW3.tex:196** — `For this one note that $||f||=\sup_{||x||=1}|f(x)|$. Or that it is the supremum of all vectors of unit length. Since it is a supremum we can get arbitrarily close to it with some $u$ this means that we can get within $\epsilon ||f||$ distance or $f(u)\geq ||f||-\epsilon ||f||=(1-\epsilon)||f||$ where $u$ is unit length by definition of norm.``
- **TODOs.md:28** — `- **functional_analysis/HW3.tex:198** — `now note that``
- **TODOs.md:29** — `- **functional_analysis/HW3.tex:240** — `This is a continuous function and satisfies $x(0)=0,\norm{x}=1$ for $a\in (0,1]$. and note that:``
- **TODOs.md:30** — `- **functional_analysis/HW3.tex:253** — `Note that since z is bounded (by continuity on compact subset):``
- **TODOs.md:31** — `- **functional_analysis/1.1-1.3.md:48** — `\text{note: } f'(t)>0\\``
- **TODOs.md:32** — `- **functional_analysis/1.1-1.3.md:92** — `First three properties are easy to check. For the triangle inequality just bootstrap off the triangle inequality for scalars. Note that if its true for all t in A then its certainly true for the sup``
- **TODOs.md:33** — `- **functional_analysis/1.1-1.3.md:114** — `Note that the sphere may not have anything in it. Take the discrete metric space as an example. Then``
- **TODOs.md:34** — `- **functional_analysis/HW4.tex:64** — `We show there is some operator that is not bounded. Take some arbitrary hamel basis of $X$. Note that in general this basis will be infinitely dimensional, but we can take a subset of this basis that is countable.``
- **TODOs.md:35** — `- **functional_analysis/HW4.tex:73** — `Take $x_n$ as given in the problem and define $y_n=(y,y,y,\dots)$. From here note that $\langle x_n,y_n\rangle = \langle x_n, y\rangle \rightarrow \langle x, y\rangle $. However``
- **TODOs.md:36** — `- **functional_analysis/HW4.tex:112** — `first note that if $A\subset B$ then $B^\perp\subset A\perp$. To prove this assume that $b\in B\perp$ so $b\perp d\in B$ in particular $b\perp a\in A$ so $b\in A^{\perp}$. From here note that if $M\subset Y$ then $Y^\perp \subset M^\perp$. But now we can do this agian to obtain that $(M^{\perp})^\perp\subset (Y^{\perp})^\perp$. However since Y is closed we know that $Y=(Y^\perp)^\perp$ so we have that:``
- **TODOs.md:37** — `- **functional_analysis/HW4.tex:116** — `% NOTE: Taking the perp of a subset inclusion reverses the subset inclusion``
- **TODOs.md:38** — `- **functional_analysis/HW4.tex:126** — `Note that this has the same minimizer as $||x-y||$ then:``
- **TODOs.md:39** — `- **functional_analysis/HW4.tex:130** — `note that in minimizing this we only need to minimize the $\beta$ so we can actually ignore the first term x since it does not depend on beta:``
- **TODOs.md:40** — `- **functional_analysis/HW4.tex:144** — `now note that this last term also has no dependence on $\beta_k$ so we can ignore it again:``
- **TODOs.md:41** — `- **functional_analysis/2.10.md:13** — `Note this is different hatn earlier because the algebraic dual is not necessarily bounded.``
- **TODOs.md:42** — `- **functional_analysis/HW1.tex:15** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:43** — `- **functional_analysis/HW1.tex:62** — `From this note that $D(A,B)=\inf_{\substack{a\in A\\b\in B}}d(a,b)=0$. If this were a metric that would mean that $A=B$, but that is clearly not the case by construction. So this is not a metric.``
- **TODOs.md:44** — `- **functional_analysis/HW1.tex:129** — `First note that``
- **TODOs.md:45** — `- **functional_analysis/HW1.tex:136** — `Note we were able to express the distance between $x(b),x(a)$ in terms of the distance between the two functions themselves. Since $x_n\rightarrow x$ we can choose N such that for $n>N,d(x_n,x)<\epsilon/2$``
- **TODOs.md:46** — `- **functional_analysis/1.4-1.6.md:74** — `<!-- TODO: Practice Proving me  -->``
- **TODOs.md:47** — `- **functional_analysis/1.4-1.6.md:122** — `Additionally note``
- **TODOs.md:48** — `- **functional_analysis/1.4-1.6.md:140** — `Note that in general convergent $\implies$ cauchy but not the other way around.``
- **TODOs.md:49** — `- **functional_analysis/HW2.tex:85** — `% TODO: Think Cauchy-shwartz``
- **TODOs.md:50** — `- **functional_analysis/HW2.tex:94** — `Note that since the absolute valiue function is continuous, we can take limits here and obtain"``
- **TODOs.md:51** — `- **functional_analysis/HW2.tex:118** — `Note that we do not have the scalar preservation here. So it is not induced by a norm.``
- **TODOs.md:52** — `- **functional_analysis/2.1-2.4.md:32** — `#### Note``
- **TODOs.md:53** — `- **functional_analysis/2.1-2.4.md:79** — `Note $B$ is not necessarily finite.``
- **TODOs.md:54** — `- **functional_analysis/2.1-2.4.md:83** — `#### Note``
- **TODOs.md:55** — `- **functional_analysis/2.1-2.4.md:117** — `<!-- TODO: What are good books to read on more advanced functional analysis not 6210 -->``
- **TODOs.md:56** — `- **functional_analysis/2.1-2.4.md:149** — `Note that X is complete iff (absolute convergence implies convergence). This is a characterization of completeness.``
- **TODOs.md:57** — `- **functional_analysis/2.1-2.4.md:174** — `$s=|\alpha_1|+\dots+|\alpha_n|$ Note that if $s=0$ then this holds trivially since that implies $|\alpha_i|=0$.``
- **TODOs.md:58** — `- **functional_analysis/2.1-2.4.md:206** — `<!-- TODO: The idea here is that we decompose any cauchy sequence in terms of the basis vectors. We then show that this gives us a cauchy sequence of coefficients. By completeness of $\R$ we can then identify a candidate limit for each coeff. Use this limit as the limit of the cauchy sequence. -->``
- **TODOs.md:62** — `- **numerical_linear_alg/HW5.pdf:3927** — `Qo^/э1,{6PJwc(-x;'dщM%&PlF")LW-bh{˵mK	l\]f=nOTEkJp qPQ+,fZzxq'(z5׫@Wo{-H6cӏ/BIϭPɍ``
- **TODOs.md:63** — `- **numerical_linear_alg/alorithms.md:11** — `- We typically can choose the base, Note that the maximum digit must be strictly smaller than the base.``
- **TODOs.md:64** — `- **numerical_linear_alg/alorithms.md:118** — `note that:``
- **TODOs.md:65** — `- **numerical_linear_alg/alorithms.md:175** — `<!-- NOTE: Floating point will not be on the midterm, but there will be one question on conditioning. -->``
- **TODOs.md:66** — `- **numerical_linear_alg/alorithms.md:176** — `The difference between this exercise and the last is that we could wiggle y. In this case we cannot wiggle one. Note that this is a forward stable algorithm.``
- **TODOs.md:67** — `- **numerical_linear_alg/alorithms.md:197** — `Note if the matrix is normal. Then the norm of this matrix is literally 1 and awesome.``
- **TODOs.md:68** — `- **numerical_linear_alg/book.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:69** — `- **numerical_linear_alg/book.tex:111** — `From here I will note without proof that for $f(x)=q^*x$ we have $\tilde f(x)=q^*x+m q^*x O(\epsilon)$. We then note that the $i,j$th entry of $\tilde{QA}-QA$ is then:``
- **TODOs.md:70** — `- **numerical_linear_alg/book.tex:128** — `Note that if we compute the QR decomposition using housholder transformations, that amounts to multiplication by a unitary matrix at each step. Thus obtaining the QR decomposition and solving for $Q^*b$ is actually backwards stable by what we just proved. The book also proves that backsubstitution is stable (I will not go into details)``
- **TODOs.md:71** — `- **numerical_linear_alg/SVD.md:66** — `Note I left off the last n-1 entries of the vector because we will not be using them.``
- **TODOs.md:72** — `- **numerical_linear_alg/SVD.md:68** — `Now note that since these two must be equal we know that $\sum |T_{1j}|^2=|T_{11}|^2$. Thus $T_{1j}=0$ for $j\neq 1$. From this we immidiately get equality above.``
- **TODOs.md:73** — `- **numerical_linear_alg/SVD.md:157** — `The number of zero eigenvalues is the number of zero singular values. Note much related``
- **TODOs.md:74** — `- **numerical_linear_alg/HW5.tex:62** — `This one is fun note that for a variable x when we want to maximize over y take:``
- **TODOs.md:75** — `- **numerical_linear_alg/HW5.tex:69** — `So we know that this quantity is always upper bounded by $\frac{||A^*x||}{||x||_2}$. However we can actually choose a y that achieve this bound. Note that for cauchy shwarts equality is achieve if one vector is a constant multiple of the other. There are two cases to consider now.``
- **TODOs.md:76** — `- **numerical_linear_alg/HW5.tex:86** — `before we move one we would like to note that in general we have that $||T^{-1}y||\leq ||T^{-1}||||y||$ for invertible T we have that $y=Tx,x=T^{-1}y$ so:``
- **TODOs.md:77** — `- **numerical_linear_alg/HW5.tex:101** — `note that since A is finite and invertible $A^{-*}$ has a finite norm and namely there is an z that achieve that bound such that $\frac{||A^{-*}z||}{||z||}=||A^{-*}||$. take that z then we have that:``
- **TODOs.md:78** — `- **numerical_linear_alg/HW5.tex:105** — `so we found a $x=A^{-*}z$ that achieves that bound. thus the $\inf_x\frac{||A^*x ||}{||x||_2}=\frac{1}{||A^{-*}||}$. Note that we are doing this in the two norm. So the largest singular value of $A^{-*}$ is the smallest singluar value of $A^*$ which is the smallest singular value of A (excluding zero singular values) so this just turns out to be $\sigma_\text{min}$ of A.``
- **TODOs.md:79** — `- **numerical_linear_alg/HW5.tex:122** — `To prove this first note that we can obtain all of the nonzero singular values of A from eigenvalues of either $AA^T$ or $A^TA$. To prove this note (taking the reduced form):``
- **TODOs.md:80** — `- **numerical_linear_alg/HW5.tex:126** — `from here note that since $U$ is $m\times r$ then $U^TU=I_r$ so:``
- **TODOs.md:81** — `- **numerical_linear_alg/HW5.tex:163** — `let $\epsilon >0$ remember that the two norm of a matrix is simply its largest singular value. Take the svd of a matrix of rank r. $A=\sum_{k=1}^r\sigma_ku_kv_k^*$. Take the fullrank completion of u and v by just setting the remaining singular values to zero if any are zero $A=\sum_{k=1}^{\min(n,m)}\sigma_ku_kv_k^*$. Set $B=\sum_{k=1}^{\min(n,m)-1}\sigma_ku_kv_k^*+(\sigma_{\min(n,m)}+\epsilon)u_{\min(n,m)}v_{\min(n,m)}^*$. (Note if A is not full rank this is just multiplied by epsilon, but since we would have set it to zero it sthe same).``
- **TODOs.md:82** — `- **numerical_linear_alg/HW5.tex:173** — `Now take an arbitary matrix norm note that:``
- **TODOs.md:83** — `- **numerical_linear_alg/HW5.tex:188** — `Recall that unitary matrices satisfy $UU^H=U^HU=I$ so they are normal and as a result are unitarily diagonalizable. Furthremore note that all of their eigenvalues have magniture one:``
- **TODOs.md:84** — `- **numerical_linear_alg/HW5.tex:193** — `for some eigenvector $v$. note that since this was nonzero that means that $|\lambda|^2=1$ so they all have absolute magnitude one. as a result let each eigenvalue be $\lambda_j$ note that we can write this in polar form as $\lambda_j=e^{i \theta_j}$ for some theta since they are magnitude one (these thetas are real angles). then:``
- **TODOs.md:85** — `- **numerical_linear_alg/HW5.tex:203** — `Note that earlier we have proven that if A matrix is hermitian positive definite it has a square root. take $\sqrt{A^*A}=S$ namely $V\Sigma V^T$ where $\Sigma$ is the square roots of hte eigenvalues so that $V\Sigma V^TV\Sigma^T V^T=V\Sigma^2V^T$ is the eigenvalue decomposition (we can do this since $A^*A$ is positive semidefinite and hermitian, so this square root is also positive semidefinite). Note this is also hermitian. but note that V is literally the svd right singular vectors of A so take:``
- **TODOs.md:86** — `- **numerical_linear_alg/HW5.tex:207** — `now note that if we took the full svd of A then $U,V$ are both unitary so $UV^T$ is also unitary. By part one we can write this as $e^{i\Theta}=UV^T$ so then:``
- **TODOs.md:87** — `- **numerical_linear_alg/HW5.tex:240** — `note that $V^T$ is an $r\times n$ matrix with orthonormal rows so $V^TV$ is $r\times r$ identity:``
- **TODOs.md:88** — `- **numerical_linear_alg/HW5.tex:242** — `from here note that $U$ is an $m\times r$ matrx with orthonormal collumns so $U^TU$ is the identity $r\times r$:``
- **TODOs.md:89** — `- **numerical_linear_alg/HW5.tex:311** — `With this problem I loaded in all of the images and stacked their flattened versions into a matrix. I then took the svd like in the previous problem and kept only the first k nonsingular values before multiplying hte matrix back together. Note that in this case it was really important that I computed the reduced svd in numpy so I didn't crach my computer.``
- **TODOs.md:90** — `- **numerical_linear_alg/HW3.tex:61** — `Note that by problem 4 we know that any matrix is orthonormally similar to an upper triangular matrix with the eigenvalues on the diagonal. So take $A$:``
- **TODOs.md:91** — `- **numerical_linear_alg/HW3.tex:65** — `Now note:``
- **TODOs.md:92** — `- **numerical_linear_alg/HW3.tex:88** — `to do this take an arbitrary eigenpair $(\lambda,v)$ then note that:``
- **TODOs.md:93** — `- **numerical_linear_alg/HW3.tex:98** — `now note that we chose $i$ such that $v_i>v_j$ for any other J this means that $\frac{v_j}{v_i}<1$ thus:``
- **TODOs.md:94** — `- **numerical_linear_alg/HW3.tex:114** — `Easy proof: Because we proved it in four we know every matrix is unitarily similar to an upper triangular matrix with the eigenvalues on the diagonal. From here note that if A is skew hermitian:``
- **TODOs.md:95** — `- **numerical_linear_alg/HW3.tex:125** — `First of all note that if $\lambda,v$ is an eigenpair of $A$ then:(choosing v to be unit length)``
- **TODOs.md:96** — `- **numerical_linear_alg/HW3.tex:137** — `Furthermore take any matrix A. We know that it has at least one eigenvalue since it has a characteristic polynomial. Take that eigenvalue $\lambda_1, v_1$ and corresponding unit eigenvector. construct $Q_1=[v_1,q_2,\dots,q_n]$ then note that:``
- **TODOs.md:97** — `- **numerical_linear_alg/HW3.tex:161** — `Note from there that this new matrix $Q_1^*AQ_1$ is also skew hermitian $-A^*=-(Q_1^*AQ_1)^*=-Q_1^*A^*Q_1=Q_1^*(-(-A))Q_1=Q_1^*AQ_1$. Thius this lower block $A_1$ is also skew hermitian. and the upper right part must be zero:``
- **TODOs.md:98** — `- **numerical_linear_alg/HW3.tex:176** — `Furthermore we can repeat this process again. Note that $A_1$ thus has at least one eigenpair $v_2,\lambda_2$ construct an orthonormal basis $U_2=[v_2,z_2,\dots,z_{n-1}]\in \R^{(n-1)\times (n-1)}$``
- **TODOs.md:99** — `- **numerical_linear_alg/HW3.tex:229** — `To prove this take any matrix A. Note that A has at least one eigenpair $\lambda_1, v_1$ because the characteristic polynomial has at least one root. construct $Q_1=[v_1,q_2,\dots, q_n]$ where we complete $v_1$ to an orthonormal basis $q_2,\dots,q_n$``
- **TODOs.md:100** — `- **numerical_linear_alg/HW3.tex:261** — `We can then note that $A_1$ also has at least one eigenpair by the same argument as before. Call this $\lambda_2,v_2$. Complete $v_2$ to an orthonormal basis of $\R^{(n-1)\times (n-1)}$.``
- **TODOs.md:101** — `- **numerical_linear_alg/HW3.tex:275** — `From there note that:``
- **TODOs.md:102** — `- **numerical_linear_alg/HW3.tex:332** — `From here note that since eigenvalues are invariant under unitary transformation ($U^*AU(U^*v)=U^*Av=U^*\lambda v=\lambda U^*v$, so any eigenvalue $\lambda$ of A with eigenvector $v$ is also a eigenvalue of this new matrix with eigenvector $U^*v$). The eigenvalues of A are the eigenvalues of $T$ which we can just read off of the diagonal.``
- **TODOs.md:103** — `- **numerical_linear_alg/HW3.tex:338** — `a) To show this first note that $\sup |W(A)|=\sup_{x\neq 0}|\frac{\langle Ax,x\rangle}{\norm{x}^2}|$ from here clearly note that:``
- **TODOs.md:104** — `- **numerical_linear_alg/HW3.tex:350** — `So the first inequality is true furthremore note that by cuachy shwartz:``
- **TODOs.md:105** — `- **numerical_linear_alg/HW3.tex:359** — `b) so note that W is a set function so we will view how this operates on arbitrary object in the set. Let $a\in W(e^{i \theta}A)$ that means $a=\frac{\langle v, e^{i\theta}Av\rangle}{\norm{v}^2}$ for some v. Which mean:``
- **TODOs.md:106** — `- **numerical_linear_alg/HW3.tex:402** — `% TODO: This technically traces out a much larger shape``
- **TODOs.md:107** — `- **numerical_linear_alg/diagonalizabilty.md:124** — `Note that if A is hermitian then the numerical range is literally just a thing on the real line. Suppose that $||x||=1$ then $R_A(x)=x^*Ax=x^*U^*\Lambda Ux$ define $c=Ux$ then $R_A(x)=c^*\Lambda c=\sum \lambda_j |c_j|^2$ so this is always a real number. Order that $\lambda_1<\lambda_2<\dots\leq \lambda_n$ then that means that the raleigh quotient is a convex combination of things. so they are always greater than the smallest and larger than the greatest:``
- **TODOs.md:108** — `- **numerical_linear_alg/HW4.tex:86** — `Note I left off the last n-1 entries of the vector because we will not be using them.``
- **TODOs.md:109** — `- **numerical_linear_alg/HW4.tex:88** — `Now note that since these two must be equal we know that $\sum |T_{1j}|^2=|T_{11}|^2$. Thus $T_{1j}=0$ for $j\neq 1$. From this we immidiately get equality above.``
- **TODOs.md:110** — `- **numerical_linear_alg/HW4.tex:134** — `Then note that:``
- **TODOs.md:111** — `- **numerical_linear_alg/HW4.tex:139** — `from here note that this is the eigenvalue decomposition of $A^*A$ and $\Lambda*=\Lambda$ because all of the eigenvalues are real. Then note that the singular values are:``
- **TODOs.md:112** — `- **numerical_linear_alg/HW4.tex:162** — `Because every matrix has an singular value decomposition. Note that $\Sigma^*=\Sigma$ since they are all real and positive. Also note that $V^*V=I$ so:``
- **TODOs.md:113** — `- **numerical_linear_alg/HW4.tex:192** — `And remember that the two norm of a matrix is the largest singular value (I think we proved this but if not note that since the two norm is invariant under unitary transformation $\norm{A}=\norm{\Sigma}$ and the norm of that diagonal (even if rectangular) matrix is just the largest entry on the diagonal). so``
- **TODOs.md:114** — `- **numerical_linear_alg/HW4.tex:248** — `Here can use a cheap trick note:``
- **TODOs.md:115** — `- **numerical_linear_alg/HW4.tex:253** — `Note that if we convert this into the $\sum ||(I-P_V)a_j+P_Va_j||_2^2$ we can apply pythagoras to each element in turn and then convert back to get:``
- **TODOs.md:116** — `- **numerical_linear_alg/HW3.log:265** — `\OT1/cmr/m/n/12 From here note that since eigen-val-ues are in-vari-ant un-der uni-tary trans-for-ma-tion ($\OML/cmm/m/it/12 U[]AU\OT1/cmr/m/n/12 (\OML/cmm/m/it/12 U[]v\OT1/cmr/m/n/12 ) =``
- **TODOs.md:117** — `- **numerical_linear_alg/HW1.tex:15** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:118** — `- **numerical_linear_alg/HW1.tex:71** — `From here note that $R_{k,:}$ is just the kth row of R and $C_{:,l}$ is merely the lth collumn of C. Thus we are just taking an inner product here between the kth row of R and the lth column of C``
- **TODOs.md:119** — `- **numerical_linear_alg/HW1.tex:78** — `b) to do this we follow the definition note that:``
- **TODOs.md:120** — `- **numerical_linear_alg/HW1.tex:122** — `note that since A is invertible $Ax=0$ iff $x=0$ thus we know that if $x\neq 0,Ax=y\neq 0$:``
- **TODOs.md:121** — `- **numerical_linear_alg/HW1.tex:140** — `First note that``
- **TODOs.md:122** — `- **numerical_linear_alg/HW1.tex:146** — `Now note that:``
- **TODOs.md:123** — `- **numerical_linear_alg/HW1.tex:154** — `For the c inequality choose $x=e_1$ Note that $\norm{e_1}_1=1$ and $\norm{e_1}_2=\sqrt{1+0+0+\dots}=1$, thus $\norm{x}_1=\norm{x}_2$``
- **TODOs.md:124** — `- **numerical_linear_alg/HW1.tex:166** — `Note that since we need to take a supremum over all possible x values we can pick an x that achieves this bound namely $e_k$ where k corresponds to the largest collumn sum thus:``
- **TODOs.md:125** — `- **numerical_linear_alg/HW1.tex:171** — `To prove the infinity norm statement note that:``
- **TODOs.md:126** — `- **numerical_linear_alg/HW1.tex:192** — `To prove this take the definition of the induced norm (Note let $A\in \R^{m\times k}, B\in \R^{k\times n}$)``
- **TODOs.md:127** — `- **numerical_linear_alg/HW1.tex:206** — `For the frobenius norm note that:``
- **TODOs.md:128** — `- **numerical_linear_alg/HW2.tex:15** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:129** — `- **numerical_linear_alg/HW2.tex:67** — `So $Ab_k=e_k$. From this note that because of this we have $(Ab_k)_i=\sum_{j=1}^{i}A_{ij}(b_k)_j=0$  For $i< k$ (Note that since A is lower triangular we only sum up to i). In particular if $i=1<k$ then:``
- **TODOs.md:130** — `- **numerical_linear_alg/HW2.tex:160** — `To prove this Assume the the projector is hermitian then, Note that $P$ projects to the range and $I-P$ projects to the null space. We show that any two vectors in this are orthogonal``
- **TODOs.md:131** — `- **numerical_linear_alg/HW2.tex:168** — `To prove the other direction. Assume that the range and null space are orthogonal. construct and orthonormal basis for the range and null space note that since the dimension of range and null space add up to the dimension of the whole space (and they are orthogonal by assumption) then this consitutes an orthonormal basis for the whole space``
- **TODOs.md:132** — `- **numerical_linear_alg/HW2.tex:172** — `From this note that if a vector $q_j$ is in the range of P then:``
- **TODOs.md:133** — `- **numerical_linear_alg/HW2.tex:181** — `call this matrix Q then note that (if $q_k$) is in the range subseciton``
- **TODOs.md:134** — `- **numerical_linear_alg/HW2.tex:197** — `So P is thus hermitian since $P^*=(Q_kQ_k^*)^*=Q_kQ_k^*=P$. (Note that here $Q_k$ is Q excluding the last $k+1,n$ collumns).``
- **TODOs.md:135** — `- **numerical_linear_alg/HW2.tex:204** — `As an aside. From this note that if a vector $v$ is in the range of any projection P then:``
- **TODOs.md:136** — `- **numerical_linear_alg/HW2.tex:215** — `Take some artbirary vector x. Note that sicne the space $\R^n$ is a direct sum of the range and null space we can write $x=v+w$ where $v\in$ the range and $w\in$ null space specified earlier.``
- **TODOs.md:137** — `- **numerical_linear_alg/HW2.tex:217** — `then note that:``
- **TODOs.md:138** — `- **numerical_linear_alg/HW2.tex:246** — `Now note that if $w^\star v=0$ then $v-u(w^\star v)=0$ a contradiction. so $w^\star v\neq 0$. and as a result``
- **TODOs.md:139** — `- **numerical_linear_alg/HW2.tex:261** — `Note that $(-(I+uw^\star)^{-1}u)=v$ is a vector so $K=vw^\star$ so it is rank one``
- **TODOs.md:140** — `- **numerical_linear_alg/HW2.tex:290** — `Note that since A is invertible $A+uw^*$ is invertibel iff $(I+A^{-1}uw^*)$ is invertible. Thus by a previous part this is invertible iff $w^*(A^{-1}u)\neq -1$ (Since this is a rank one pertubation of the identity)``
- **TODOs.md:141** — `- **numerical_linear_alg/HW2.tex:311** — `Note that``
- **TODOs.md:142** — `- **numerical_linear_alg/HW2.tex:366** — `Construct a basis for the range of $P$ call it $q_1,\dots, q_k$ and a basis for the null space of $q_{k+1},\dots,q_n$. Note that putting these two basis together constructs a basis for the whole space (however this is not necessarily a unitary basis) by the rank nullity theorem.``
- **TODOs.md:143** — `- **numerical_linear_alg/HW2.tex:368** — `From this note that if a vector $q_j$ is in the range of P then:``
- **TODOs.md:144** — `- **numerical_linear_alg/HW2.tex:428** — `Where the lower case v in this case refers to entries of $V_A$ and the $\lambda_i$ refers to eigenvalues of A.. Note that``
- **TODOs.md:145** — `- **numerical_linear_alg/HW2.tex:430** — `Now note that since each $v_{:,j}$ is an eigenvector of A with corresponding eigenvalue $\lambda_j$``
- **TODOs.md:149** — `- **numerical_linear_alg/6610 (2)/6610/HW5.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:150** — `- **numerical_linear_alg/6610 (2)/6610/HW5.tex:76** — `So $\lambda D+\lambda L+U$ is singular. Note that a diagonally dominant matrix cannot be singular. If $\lambda =1$ then this is just A which means its diagonally dominant thus we have a contradiction. Similarly for any $\lambda >1$ we have this being diagonally dominant so it is singular. Thus we must have $\lambda < 1$``
- **TODOs.md:151** — `- **numerical_linear_alg/6610 (2)/6610/HW5.tex:97** — `note that``
- **TODOs.md:152** — `- **numerical_linear_alg/6610 (2)/6610/HW4.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:153** — `- **numerical_linear_alg/6610 (2)/6610/HW4.tex:74** — `Note that we can pass the norm through because the series converges absolutley``
- **TODOs.md:154** — `- **numerical_linear_alg/6610 (2)/6610/HW4.tex:101** — `Note that:``
- **TODOs.md:155** — `- **numerical_linear_alg/6610 (2)/6610/HW4.tex:191** — `note that``
- **TODOs.md:156** — `- **numerical_linear_alg/6610 (2)/6610/HW_3.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:157** — `- **numerical_linear_alg/6610 (2)/6610/HW_3.tex:143** — `To prove this note that we can write A:``
- **TODOs.md:158** — `- **numerical_linear_alg/6610 (2)/6610/HW_3.tex:164** — `To show this first part. Note that since we have more columns than rows we know that $n-m$ of the columns can be formed by linear combinations of the first m columns. We``
- **TODOs.md:159** — `- **numerical_linear_alg/6610 (2)/6610/HW_3.tex:166** — `Perhaps we should do this using QR note that the QR factorization will looks like:``
- **TODOs.md:160** — `- **numerical_linear_alg/6610 (2)/6610/HW_3.tex:174** — `Note that the last $n-m$ cols of r will all be zero because we can form them as linear combinations of the first m collumns in the gram schmidt process.``
- **TODOs.md:161** — `- **numerical_linear_alg/6610 (2)/6610/HW_1.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:162** — `- **numerical_linear_alg/6610 (2)/6610/HW_1.tex:63** — `Note that since this is unitary we know thatthe inner product of the first row and first collumn is 1 while the inner product of the first row and ith collumn is zero. For this first statement to be true we know that $a_{11}=1/\bar{a_{11}}$. For the second statement this can only be true if the collumn below $a_{11}$ is all zero (to cancel out to zero).``
- **TODOs.md:163** — `- **numerical_linear_alg/6610 (2)/6610/HW_1.tex:111** — `To prove this note that:``
- **TODOs.md:164** — `- **numerical_linear_alg/6610 (2)/6610/HW_2.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:165** — `- **numerical_linear_alg/6610 (2)/6610/HW_2.tex:77** — `Note then that:``
- **TODOs.md:166** — `- **numerical_linear_alg/6610 (2)/6610/HW_2.tex:86** — `We need to find an eigenvalue decomposition note:``
- **TODOs.md:167** — `- **numerical_linear_alg/6610 (2)/6610/HW_2.tex:110** — `Now note that``
- **TODOs.md:168** — `- **numerical_linear_alg/6610 (2)/6610/HW_2.tex:124** — `To prove this note that``
- **TODOs.md:172** — `- **numerical_linear_alg/Math6610NumericalAnalysisI/Math6610-lecturenotes-Sept21-Oct052022.pdf:95090** — `mR8բL4PF:!b	ToDO+/8+g }lqHdr\@{Gw6eX7NS(r܆5Ss6~K``
- **TODOs.md:173** — `- **numerical_linear_alg/Math6610NumericalAnalysisI/Math6610-lecturenotes-Sept30-Oct052022.pdf:19473** — `mR8բL4PF:!b	ToDO+/8+g }lqHdr\@{Gw6eX7NS(r܆5Ss6~K``
- **TODOs.md:174** — `- **numerical_linear_alg/Math6610NumericalAnalysisI/Math6610-lecturenotes-Nov082022.pdf:13826** — `үŀtodO@ƪN%x4<G1tTV1``
- **TODOs.md:178** — `- **numerical_linear_alg/Review/review.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:179** — `- **numerical_linear_alg/Review/notes.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:180** — `- **numerical_linear_alg/Review/notes.tex:62** — `So to prove the thing with matrix splits. Assume that a matrix A is irreducibly diagonally dominant. Note then that at least one row in``
- **TODOs.md:181** — `- **numerical_linear_alg/Review/notes.tex:77** — `Let A be a full ranke matrix. Let B be some rank r matrix. Let $A_r$ be the rank r approximation to A. Note that if we take one of the first $r+1$ right singular vectors of eA tn because B is only rank r we know that at least one of them lies in the null space of b. Call it index j. We will take the supremum over all unit vectors x``
- **TODOs.md:182** — `- **numerical_linear_alg/Review/notes.tex:113** — `From this we knwo that $UL^{-1}$ is unitary. However note that it is also upper triangular. That means that it is actually diagonal and that the diagonal entries must be the roots of unity. From the fact that we know that the diagonal entries of U are real and positive, we also know that the diagonal entries of $L^{-1}$ are real and positive. Thus they must be one. so:``
- **TODOs.md:186** — `- **numerical_odes/LeVeque_heat.ipynb:24** — `"note that for $U_1,U_{m}$ then:\n",``
- **TODOs.md:187** — `- **numerical_odes/LeVeque_heat.ipynb:96** — `"We next note that in the two norm that eigenvectors of this operator correspond to eigenvectors of the derivative operator evaluated at the grid points:\n"``
- **TODOs.md:188** — `- **numerical_odes/LeVeque_heat.ipynb:278** — `"note that even if we disectrize:\n",``
- **TODOs.md:189** — `- **numerical_odes/numerical_odes.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:190** — `- **numerical_odes/numerical_odes.tex:60** — `Assume that $f\in C^{(n+1)}(\R)$ then note that:``
- **TODOs.md:191** — `- **numerical_odes/numerical_odes.tex:169** — `Where $g$ is our approximation to the second order derivative. Typically when deriving this we only care about the big-O and what order it is (say $O(h^p)$) and we say that $\tau_j=O(h^p)$. Note that in this definition we assume we know u and expand each taylor series on u not $U$``
- **TODOs.md:192** — `- **numerical_odes/numerical_odes.tex:201** — `Note that then if f is a discrete sum of delta functions that the solution to the BVP is then:``
- **TODOs.md:196** — `- **numerical_odes/6620 (2)/6620/HWHW 3.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:197** — `- **numerical_odes/6620 (2)/6620/HWHW 3.tex:67** — `Ok So the idea here is we want to use a taylor expansion. Note that if we just have two points then they think:``
- **TODOs.md:198** — `- **numerical_odes/6620 (2)/6620/HWHW 3.tex:151** — `note that``
- **TODOs.md:199** — `- **numerical_odes/6620 (2)/6620/HW5.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:200** — `- **numerical_odes/6620 (2)/6620/HW5.tex:82** — `note that``
- **TODOs.md:201** — `- **numerical_odes/6620 (2)/6620/HW4.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:202** — `- **numerical_odes/6620 (2)/6620/HW4.tex:143** — `note that``
- **TODOs.md:203** — `- **numerical_odes/6620 (2)/6620/HW_1.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:204** — `- **numerical_odes/6620 (2)/6620/HW_2.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:205** — `- **numerical_odes/6620 (2)/6620/HW_2.tex:113** — `To prove it is odd. Note that this polynomial is p. Define $q(x)=-p(-x)$. Note that Q also interpolates the data. Because q is also of the same degree as p and interpolates the data they must be equal. so $p(x)=-p(-x)$``
- **TODOs.md:206** — `- **numerical_odes/6620 (2)/6620/HW_2.tex:119** — `Note the lagrange basis functions are unique in that they satisfy $l_j(x_j)=1$ for each $x_j$. and zero on the other ones. Suppose you interpolate $1$ then we know that:``
- **TODOs.md:210** — `- **odes/reading_week2.md:33** — `Note that we can often transform equations bty using an appropriate change of variables. When you do this take a new variable $y=f(x,t)$ and then just differentiate through this using the chain rule``
- **TODOs.md:211** — `- **odes/day_2.md:18** — `Note that this is a second order ode. We want to convert this to a first order system``
- **TODOs.md:212** — `- **odes/day_2.md:83** — `now note that both zeros depend on H, for $H< \frac{\gamma k}{4}$ there are two positive fixed points where $r(10 \frac{N}{k})-H=0,\implies N\pm = \frac{(r\pm \sqrt r^2-\frac{4Hr}{k} )k}{2r} $``
- **TODOs.md:213** — `- **odes/day_2.md:111** — `Note that one solution is definitely $x=0$. Another could definitely be $\frac{dx}{x^{1/3}}=dt$``
- **TODOs.md:214** — `- **odes/day_2.md:117** — `We need to think about this till after class. Note the solutions are just piece wise connections of our two solutions.``
- **TODOs.md:215** — `- **odes/existence.md:26** — `<!-- NOTE: Remark we can pass limits inside continuous functions -->``
- **TODOs.md:216** — `- **odes/existence.md:28** — `<!-- NOTE: Gronwalls says that: -->``
- **TODOs.md:217** — `- **odes/existence.md:32** — `<!-- NOTE: What are the assumptions on Gronwalls? -->``
- **TODOs.md:218** — `- **odes/stability_10.md:69** — `<!-- NOTE: This may be on the exam -->``
- **TODOs.md:219** — `- **odes/stability_10.md:82** — `for some set of jordan blocks $J$ from here note tjhat:``
- **TODOs.md:220** — `- **odes/stability_10.md:104** — `For the final case we will note that we can no longer bound the nilpotent matrix by an exponential. However since there are no exponentials anywhere (The norm of the matrix is just one). We can bound it by  a polynomial instead.``
- **TODOs.md:221** — `- **odes/stability_10.md:191** — `<!-- NOTE: This will be on the exam -->``
- **TODOs.md:222** — `- **odes/day_5.md:64** — `To prove this. Note that if the solution is ever a or b, then it will always stay at one of those, so by the previous lemma since they can't intersect. So for $x_0\in (a,b)$ the solution never reaches either of those.``
- **TODOs.md:223** — `- **odes/HW3.tex:61** — `% NOTE: ONE OF THESE WILL Be on the quals``
- **TODOs.md:224** — `- **odes/HW3.tex:71** — `% NOTE: Note that when proving things with this remember to start with the derivativeof the invariant set function applied to the flow map``
- **TODOs.md:225** — `- **odes/HW3.tex:84** — `From here note that because f is continuous on a bounded domain then we can bound it above by some $|f|<M$. Similarly for $|\nabla g|<K$ so:``
- **TODOs.md:226** — `- **odes/HW3.tex:89** — `Note that because $g(\phi_t(x))$ is small it is well approximated by a taylor  series around $x_b$ $\nabla g(\phi_t(x))\approx \nabla g(x_b)+D^2g(x_b)(\phi_t(x)-x_b)+h(\phi_t(x))(\phi_t(x)-x_b))$ note that because we are considering small $g$ we will have that $\phi_t(x)$ is close to $x_b$. From this since the peano form of the remainder approaches zero when that exact thing happens. we can choose a sufficiently small radius so that $h_(\phi_t(x))<\epsilon$  So we can plug that into our equations:``
- **TODOs.md:227** — `- **odes/HW3.tex:94** — `Note that because g is smooth then this $D^2g(x_b)$ is also bounded call this bound $N=D^2g(x_b)+\epsilon$:``
- **TODOs.md:228** — `- **odes/HW3.tex:96** — `\textbf{Remark}: Above we used a taylor series expansion to bound $|\nabla g(\phi_t(x))-\nabla g(x_b)|$ however one could also note that smooth functions on bounded sets are also lipshitz so then it immideiately follows that:``
- **TODOs.md:229** — `- **odes/HW3.tex:97** — `$|\nabla g(\phi_t(x))-\nabla g(x_b)|\leq N(\phi_t(x)-x_b)$. On a similar note I could have noted that since $\nabla g$ is lipshitz continuous on the bounded domain, then the dot product of two lipshitz functions on a bounded domain is also lipshitz. Then I could have just take $|\frac{d}{dt}g(\phi_t(x))|=|Dg(\phi_t(x))f(t,\phi_t(x))|=|Dg(\phi_t(x))f(t,\phi_t(x))-Dg(x_b)f(t,x_b)|\leq L|\phi_t(x)-x_b|$ for some constant L. Things are a lot quicker in retrospect. But either way, we go back to the main argument!``
- **TODOs.md:230** — `- **odes/HW3.tex:110** — `Note from here that this distance $|\phi_t(x)-x_b|$ is literally the definition of $g$ as the signed distance (note that its an absolute value, but we will only consider $\phi_t(x)$ that is inside or on the boundary so this is eqivalent to the signed distance). We take r small enough so $x_b$ is the unique closest point is the unique closest point.``
- **TODOs.md:231** — `- **odes/HW3.tex:146** — `b) For this part assume that we start inside the set $U$. Note that if we never approach the border then clearly our solution is invariant. However if it does approach the border all of the problems will always occur near the border because our solution is continuous. By the intermediate value theorem if it were to leave our set it would have to get near the border first. For this reason without loss of generality we consider a $x_0$ close enough to the border so our previous theorem applies. thus:``
- **TODOs.md:232** — `- **odes/HW3.tex:152** — `c) For the firs part note that at time zero (if $x_0\in \partial U$):``
- **TODOs.md:233** — `- **odes/HW3.tex:156** — `Note that because we are doing time $t=0$ I just plugged in $\phi_0(x_0)=x_0$``
- **TODOs.md:234** — `- **odes/HW3.tex:185** — `(Using the same notation in the slides were we are taking the derivative at the point A in the direction of B $\det'(A)(B)$). (Note that the inverse here exists because we proved it in class)``
- **TODOs.md:235** — `- **odes/HW3.tex:204** — `% NOTE: remember the derivative of the determinant``
- **TODOs.md:236** — `- **odes/HW3.tex:212** — `% NOTE: Memorize this bound``
- **TODOs.md:237** — `- **odes/HW3.tex:213** — `First note that because all of the eigenvalues of A are distinct and have negative real part then we can bound $e^{At}$ by:``
- **TODOs.md:238** — `- **odes/HW3.tex:229** — `Note that for each j $|e^{\lambda_j t}|= e^{\text{real}(\lambda) t}$``
- **TODOs.md:239** — `- **odes/HW3.tex:247** — `First note that the first term abtrarily approaches zero because of the bound on the exponential.``
- **TODOs.md:240** — `- **odes/HW3.tex:249** — `From here note that because $|g(s)|\rightarrow 0$ there is a time l when $s>l$ means $g(s)<\epsilon$ then:``
- **TODOs.md:241** — `- **odes/HW3.tex:257** — `Note that because $g(s)$ is continuous it is bounded over this compact interval say by M:``
- **TODOs.md:242** — `- **odes/HW3.tex:273** — `Note that we can always choose l to make epsilon as small as we like. So choose an arbitrarily small epsilon and we will get a corresponding finite l. Since l is still finite then the given exponentials will still approach zero after enough time.``
- **TODOs.md:243** — `- **odes/HW3.tex:301** — `% NOTE: Remember The advanced gronwall``
- **TODOs.md:244** — `- **odes/HW3.tex:308** — `Where $e^{\Lambda}$ is applied elementwise on the matrix and $u_j$ are the rows of $V^{-1}$. Note that each of these terms approach zero because they each have a negative exponential. The rate of convergence is just the eigenvalue with real part closest to zero (further to the right on the complex plane) because that will decay the slowest. This first one only relies on initial data for the coeffients of the exponentials so how high they start before they start decaying.``
- **TODOs.md:245** — `- **odes/HW3.tex:387** — `Note that the norm of that diagonal matrix is the eigenvalue with the largest real part which i denote $\lambda_j$. So thus it is proven.``
- **TODOs.md:246** — `- **odes/HW4.tex:155** — `Note that I just did the jordan form matrix exponential in my head (its just a polynomial). Combining all of these together we get:``
- **TODOs.md:247** — `- **odes/HW4.tex:277** — `Finally if $\rho^2=4\omega^2$. Then we will have to use the generalize eigenspace because we will have a degenerate eigenvalue at $-\rho/2$. to do this first note that one eigenvector remains the same $% 2 x 1 BMatrix``
- **TODOs.md:248** — `- **odes/week1.md:11** — `For energy, first multiply by $\dot x$ from the rest. Then isolate the $\dot x^2$ term from the rest. This enables us to use positivity. We then can use integrating factors on the other side to better under stand things. note we will usually have a $\frac{d}{dt}(\dot x/2)^2=\ddot x\dot x$ term as well as a``
- **TODOs.md:249** — `- **odes/non-autonomous_11.md:27** — `Note that $\Phi(t)$ maps the point from the initial condition to its position at time t. So then $\Phi(t_0)$ maps from the point it is at at zero to its point at $t_0$ whereas the inverse maps $t_0$ to its point at the initial condition.``
- **TODOs.md:250** — `- **odes/matrix_exponentials_9.md:33** — `Let $Q=[\text{re}(v),\text{im}(b)]$ note that we can express $v, \overline{v}$ interms of these:``
- **TODOs.md:251** — `- **odes/matrix_exponentials_9.md:38** — `now note that $\lambda = \rho + i\omega, v= re(v)+i im(v)$``
- **TODOs.md:252** — `- **odes/flowmaps.md:34** — `Note that we can do this because its globally lipshitz``
- **TODOs.md:253** — `- **odes/flowmaps.md:83** — `note that the solution is:``
- **TODOs.md:254** — `- **odes/flowmaps.md:127** — `<!-- NOTE: This will be in the exam -->``
- **TODOs.md:255** — `- **odes/HW2.tex:15** — `% looks normal.  Note that 1.1=1/.9090909...``
- **TODOs.md:256** — `- **odes/HW2.tex:60** — `Note for this problem we want to find the Lipshitz bound L. This is the same as bounding the norm of the derivative with respect to mu. Then take:``
- **TODOs.md:257** — `- **odes/HW2.tex:89** — `Alternatively you can do a different method with derivative tricks, note this is not my main answer but is included for completeness.``
- **TODOs.md:258** — `- **odes/HW2.tex:91** — `For this problem note that we can write the integral form:``
- **TODOs.md:259** — `- **odes/HW2.tex:154** — `% NOTE: From this firstr problem. I learned that if I have multiple components I can use the triangle inequality first to separate them. Then use the multivariate calculus trick, Then gronwalls advanced inequality.``
- **TODOs.md:260** — `- **odes/HW2.tex:156** — `% NOTE: from the second problem. just follow proofs through``
- **TODOs.md:261** — `- **odes/HW2.tex:188** — `Now note that becaue $p$ is increasing $\frac{1}{p}$ is decreasing. As a result $\int_0^\frac{h}{2}\frac{1}{p(s)}\geq \int_\frac{h}{2}^h \frac{1}{p(s)}$. From this we can gather that``
- **TODOs.md:262** — `- **odes/HW2.tex:194** — `From here note that the inequality we have derived``
- **TODOs.md:263** — `- **odes/HW2.tex:220** — `Note that for small $u(t)$ $|\log(u(t))|=-\log(u(t))$ for $|u(t)|<1$ while for $u(t)>1$ it is $\log(u(t))$. Furtherome not that because $\rho$ is positive and increasing we have that $u(t)$ is strictly increasing. (It is a positive number plus the integral of a positive number)``
- **TODOs.md:264** — `- **odes/HW2.tex:236** — `Here is a graph of the normal lipshitz bound $e^{Lt}|x_0-y_0|$ in red verses the new bound $e^{e^{Lt}\frac{1}{1-\log(|x_0-y_0|))}-1}$ in blue. You can see that the new bound grows way faster! This can be seen in the equation just because we will have an exponential to a positive exponential (because $\frac{1}{1-\log(|x_0-y_0|)}>0$ in this case). Note for the graph I set $x_0=0,y_0=0.1,L=1$``
- **TODOs.md:265** — `- **odes/HW2.tex:267** — `Here is a graph of the normal lipshitz bound $e^{Lt}|x_0-y_0|$ in red verses the new bound $e^{e^{Lt}(1+\log|x_0-y_0|)-1} $ in blue. You can see that the new bound grows way faster! This can be seen in the equation just because we will have an exponential to a positive exponential (because $1+\log(|x_0-y_0|)>0$ in this case). Note for the graph I set $x_0=0,y_0=1.1,L=1$``
- **TODOs.md:266** — `- **odes/floquet_12-13.md:34** — `Let $\Phi(t)$ be the fundamental matrix solution note:``
- **TODOs.md:267** — `- **odes/floquet_12-13.md:43** — `First note that M is invertible. Secondly note the previous equality``
- **TODOs.md:268** — `- **odes/floquet_12-13.md:67** — `First note that we have the following relationship:``
- **TODOs.md:269** — `- **odes/floquet_12-13.md:71** — `This implies that $\chi(t+kT)=\mu_j^k\chi_j(t)$. Note this either diverges to infinity or converges to zero.``
- **TODOs.md:270** — `- **odes/floquet_12-13.md:98** — `note chi could be complex but he said to ignore that for now because it will cancel out later. This also doesn't quite work but he says it will work out. if this is real then this works for a period of 2T because the angle will just be -1 so two of them will be 1.``
- **TODOs.md:274** — `- **odes/volume_3_textbook/V3Ch11-W2024.pdf:22037** — `G6uټL@z9Jǂim'X'.*Wε}Of<,	R	lOODr#	σdOU'z)rc<5%~yWH*`jԱr}y˂Iqle{&L'Xvh3^M|u\m뼜镚l'XwV%T<_e;|.>:-vuqĪ>.]߳i_1ͤF.^todo-O2u-1]P4Z@tyAk[^6[[U<lXG>!}1xV+FXYB?MȈNԗ}D.nb&iGc`L>_E.Vl'W+T|;0G69v H>zߩyOM[ލAڿ	?7@;/Ai6ĄyfK8ÊAjO"Ʒٷ!s\?|EMZ=y*C;\H\>`$|@V;OkW!`5nCkI6Ǵ&7o.Ax4_=7)i]|>£	3x@O@sGqBQTL~``
- **note_creator.py:7** — `TAGS = ["TODO", "FIXME", "NOTE"]`
- **note_creator.py:30** — `md.write("# Project TODO / FIXME / NOTE Summary\n\n")`

## functional_analysis

- **functional_analysis/3.1.md:27** — `<!-- NOTE: This will be on the exam -->`
- **functional_analysis/3.1.md:140** — `note that $2|(y_n+y_m)/2-x|\geq 2d(x,M)$`
- **functional_analysis/3.1.md:181** — `then note that $Y^\perp = \text{span}(Y)^\perp, Y^\perp$ is also closed`
- **functional_analysis/3.1.md:192** — `<!-- NOTE: This may be on the exam -->`
- **functional_analysis/3.1.md:202** — `in the other direction assume that the perp is zero. note then that we can write anything as the closure of the span of M and its perp. Since the perp  is zero $x=y$ so we can write anything as something in the closure of the span. So they are equal`
- **functional_analysis/day_4.md:4** — `<!-- TODO: Re-read me later, write me down-->`
- **functional_analysis/day_4.md:5** — `<!-- FIXME: In the proof of the completed space, How can a sequence be cauchy if it is constant? Isn't that mute? -->`
- **functional_analysis/HW3.tex:62** — `Take some arbitrary cauchy sequence. Note that you can write it via telescoping as:`
- **functional_analysis/HW3.tex:102** — `From here note that we can always choose $n$ large enough so that the first term is less than $\epsilon/2$ this just follows from the definition of the shauder basis.`
- **functional_analysis/HW3.tex:111** — `So we can get arbitrarily close to anything in x with a thing from P. Now note that P is countable. This follows from the fact that $Q$ is countable and we are only taking finite sums over the countable shauder basis.`
- **functional_analysis/HW3.tex:118** — `To do this note first that by problem 5 the operator defined by $y=(\eta_j)$ where $y=Tx,\eta_j=\xi_j/j,x=\xi_j$ is linear and bounded in other words if:`
- **functional_analysis/HW3.tex:125** — `To do this note that if $y\in R(T)$ then there is an $x$ such that $y_j=\frac{x_j}{j}$ furthermore we know that $x_j$ is in $l^\infty$ so $\max_j x_j=\max_jy_j j<\infty$`
- **functional_analysis/HW3.tex:144** — `Choose $K>M, K\in \Z$. from here take the vector $y=(1,\dots,1,0,\dots)$ where the ones take up $K$ positions. Note that $y\in R(T)$ just take $x=(1,2,\dots, K,0,\dots)$ clearly $x\in l^\infty$ so that $Tx=y$.`
- **functional_analysis/HW3.tex:146** — `from here note that $T^{-1}y=x$ from what we just showed and that $\max_j |x_j|=K$ however that means that:`
- **functional_analysis/HW3.tex:150** — `Furthermore note that $y$ is unit norm so:`
- **functional_analysis/HW3.tex:160** — `So the idea for this problem is that we actually need to create a basis. Choose the basis for x so that we have a basis $\{z_1,\dots z_k\}$ for Z and a separate basis for $X-Z$ $b_{k+1},\dots b_n$ (Note that both of these are nonepty by the fact that this is a proper subspace). Choose $b_{k+1}=x_0$ (we are allowed to do this since we can just pull other linearly independent vectors in). First notice that this is a bsis for the whole space because any thing in X is either in Z or not in Z ($X=(X\cap Z^c)\cup (X\cap Z)$). From here define the linear functional by:`
- **functional_analysis/HW3.tex:191** — `now note that $0\in N(f), f(0)=0*f(0)=0$ so that $d(x,Y)\leq d(x,\{0\})=||x||$ thus:`
- **functional_analysis/HW3.tex:196** — `For this one note that $||f||=\sup_{||x||=1}|f(x)|$. Or that it is the supremum of all vectors of unit length. Since it is a supremum we can get arbitrarily close to it with some $u$ this means that we can get within $\epsilon ||f||$ distance or $f(u)\geq ||f||-\epsilon ||f||=(1-\epsilon)||f||$ where $u$ is unit length by definition of norm.`
- **functional_analysis/HW3.tex:198** — `now note that`
- **functional_analysis/HW3.tex:240** — `This is a continuous function and satisfies $x(0)=0,\norm{x}=1$ for $a\in (0,1]$. and note that:`
- **functional_analysis/HW3.tex:253** — `Note that since z is bounded (by continuity on compact subset):`
- **functional_analysis/1.1-1.3.md:48** — `\text{note: } f'(t)>0\\`
- **functional_analysis/1.1-1.3.md:92** — `First three properties are easy to check. For the triangle inequality just bootstrap off the triangle inequality for scalars. Note that if its true for all t in A then its certainly true for the sup`
- **functional_analysis/1.1-1.3.md:114** — `Note that the sphere may not have anything in it. Take the discrete metric space as an example. Then`
- **functional_analysis/HW4.tex:64** — `We show there is some operator that is not bounded. Take some arbitrary hamel basis of $X$. Note that in general this basis will be infinitely dimensional, but we can take a subset of this basis that is countable.`
- **functional_analysis/HW4.tex:73** — `Take $x_n$ as given in the problem and define $y_n=(y,y,y,\dots)$. From here note that $\langle x_n,y_n\rangle = \langle x_n, y\rangle \rightarrow \langle x, y\rangle $. However`
- **functional_analysis/HW4.tex:112** — `first note that if $A\subset B$ then $B^\perp\subset A\perp$. To prove this assume that $b\in B\perp$ so $b\perp d\in B$ in particular $b\perp a\in A$ so $b\in A^{\perp}$. From here note that if $M\subset Y$ then $Y^\perp \subset M^\perp$. But now we can do this agian to obtain that $(M^{\perp})^\perp\subset (Y^{\perp})^\perp$. However since Y is closed we know that $Y=(Y^\perp)^\perp$ so we have that:`
- **functional_analysis/HW4.tex:116** — `% NOTE: Taking the perp of a subset inclusion reverses the subset inclusion`
- **functional_analysis/HW4.tex:126** — `Note that this has the same minimizer as $||x-y||$ then:`
- **functional_analysis/HW4.tex:130** — `note that in minimizing this we only need to minimize the $\beta$ so we can actually ignore the first term x since it does not depend on beta:`
- **functional_analysis/HW4.tex:144** — `now note that this last term also has no dependence on $\beta_k$ so we can ignore it again:`
- **functional_analysis/2.10.md:13** — `Note this is different hatn earlier because the algebraic dual is not necessarily bounded.`
- **functional_analysis/HW1.tex:15** — `% looks normal.  Note that 1.1=1/.9090909...`
- **functional_analysis/HW1.tex:62** — `From this note that $D(A,B)=\inf_{\substack{a\in A\\b\in B}}d(a,b)=0$. If this were a metric that would mean that $A=B$, but that is clearly not the case by construction. So this is not a metric.`
- **functional_analysis/HW1.tex:129** — `First note that`
- **functional_analysis/HW1.tex:136** — `Note we were able to express the distance between $x(b),x(a)$ in terms of the distance between the two functions themselves. Since $x_n\rightarrow x$ we can choose N such that for $n>N,d(x_n,x)<\epsilon/2$`
- **functional_analysis/1.4-1.6.md:74** — `<!-- TODO: Practice Proving me  -->`
- **functional_analysis/1.4-1.6.md:122** — `Additionally note`
- **functional_analysis/1.4-1.6.md:140** — `Note that in general convergent $\implies$ cauchy but not the other way around.`
- **functional_analysis/HW2.tex:85** — `% TODO: Think Cauchy-shwartz`
- **functional_analysis/HW2.tex:94** — `Note that since the absolute valiue function is continuous, we can take limits here and obtain"`
- **functional_analysis/HW2.tex:118** — `Note that we do not have the scalar preservation here. So it is not induced by a norm.`
- **functional_analysis/2.1-2.4.md:32** — `#### Note`
- **functional_analysis/2.1-2.4.md:79** — `Note $B$ is not necessarily finite.`
- **functional_analysis/2.1-2.4.md:83** — `#### Note`
- **functional_analysis/2.1-2.4.md:117** — `<!-- TODO: What are good books to read on more advanced functional analysis not 6210 -->`
- **functional_analysis/2.1-2.4.md:149** — `Note that X is complete iff (absolute convergence implies convergence). This is a characterization of completeness.`
- **functional_analysis/2.1-2.4.md:174** — `$s=|\alpha_1|+\dots+|\alpha_n|$ Note that if $s=0$ then this holds trivially since that implies $|\alpha_i|=0$.`
- **functional_analysis/2.1-2.4.md:206** — `<!-- TODO: The idea here is that we decompose any cauchy sequence in terms of the basis vectors. We then show that this gives us a cauchy sequence of coefficients. By completeness of $\R$ we can then identify a candidate limit for each coeff. Use this limit as the limit of the cauchy sequence. -->`

## numerical_linear_alg

- **numerical_linear_alg/HW5.pdf:3927** — `Qo^/э1,{6PJwc(-x;'dщM%&PlF")LW-bh{˵mK	l\]f=nOTEkJp qPQ+,fZzxq'(z5׫@Wo{-H6cӏ/BIϭPɍ`
- **numerical_linear_alg/alorithms.md:11** — `- We typically can choose the base, Note that the maximum digit must be strictly smaller than the base.`
- **numerical_linear_alg/alorithms.md:118** — `note that:`
- **numerical_linear_alg/alorithms.md:175** — `<!-- NOTE: Floating point will not be on the midterm, but there will be one question on conditioning. -->`
- **numerical_linear_alg/alorithms.md:176** — `The difference between this exercise and the last is that we could wiggle y. In this case we cannot wiggle one. Note that this is a forward stable algorithm.`
- **numerical_linear_alg/alorithms.md:197** — `Note if the matrix is normal. Then the norm of this matrix is literally 1 and awesome.`
- **numerical_linear_alg/book.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...`
- **numerical_linear_alg/book.tex:111** — `From here I will note without proof that for $f(x)=q^*x$ we have $\tilde f(x)=q^*x+m q^*x O(\epsilon)$. We then note that the $i,j$th entry of $\tilde{QA}-QA$ is then:`
- **numerical_linear_alg/book.tex:128** — `Note that if we compute the QR decomposition using housholder transformations, that amounts to multiplication by a unitary matrix at each step. Thus obtaining the QR decomposition and solving for $Q^*b$ is actually backwards stable by what we just proved. The book also proves that backsubstitution is stable (I will not go into details)`
- **numerical_linear_alg/SVD.md:66** — `Note I left off the last n-1 entries of the vector because we will not be using them.`
- **numerical_linear_alg/SVD.md:68** — `Now note that since these two must be equal we know that $\sum |T_{1j}|^2=|T_{11}|^2$. Thus $T_{1j}=0$ for $j\neq 1$. From this we immidiately get equality above.`
- **numerical_linear_alg/SVD.md:157** — `The number of zero eigenvalues is the number of zero singular values. Note much related`
- **numerical_linear_alg/HW5.tex:62** — `This one is fun note that for a variable x when we want to maximize over y take:`
- **numerical_linear_alg/HW5.tex:69** — `So we know that this quantity is always upper bounded by $\frac{||A^*x||}{||x||_2}$. However we can actually choose a y that achieve this bound. Note that for cauchy shwarts equality is achieve if one vector is a constant multiple of the other. There are two cases to consider now.`
- **numerical_linear_alg/HW5.tex:86** — `before we move one we would like to note that in general we have that $||T^{-1}y||\leq ||T^{-1}||||y||$ for invertible T we have that $y=Tx,x=T^{-1}y$ so:`
- **numerical_linear_alg/HW5.tex:101** — `note that since A is finite and invertible $A^{-*}$ has a finite norm and namely there is an z that achieve that bound such that $\frac{||A^{-*}z||}{||z||}=||A^{-*}||$. take that z then we have that:`
- **numerical_linear_alg/HW5.tex:105** — `so we found a $x=A^{-*}z$ that achieves that bound. thus the $\inf_x\frac{||A^*x ||}{||x||_2}=\frac{1}{||A^{-*}||}$. Note that we are doing this in the two norm. So the largest singular value of $A^{-*}$ is the smallest singluar value of $A^*$ which is the smallest singular value of A (excluding zero singular values) so this just turns out to be $\sigma_\text{min}$ of A.`
- **numerical_linear_alg/HW5.tex:122** — `To prove this first note that we can obtain all of the nonzero singular values of A from eigenvalues of either $AA^T$ or $A^TA$. To prove this note (taking the reduced form):`
- **numerical_linear_alg/HW5.tex:126** — `from here note that since $U$ is $m\times r$ then $U^TU=I_r$ so:`
- **numerical_linear_alg/HW5.tex:163** — `let $\epsilon >0$ remember that the two norm of a matrix is simply its largest singular value. Take the svd of a matrix of rank r. $A=\sum_{k=1}^r\sigma_ku_kv_k^*$. Take the fullrank completion of u and v by just setting the remaining singular values to zero if any are zero $A=\sum_{k=1}^{\min(n,m)}\sigma_ku_kv_k^*$. Set $B=\sum_{k=1}^{\min(n,m)-1}\sigma_ku_kv_k^*+(\sigma_{\min(n,m)}+\epsilon)u_{\min(n,m)}v_{\min(n,m)}^*$. (Note if A is not full rank this is just multiplied by epsilon, but since we would have set it to zero it sthe same).`
- **numerical_linear_alg/HW5.tex:173** — `Now take an arbitary matrix norm note that:`
- **numerical_linear_alg/HW5.tex:188** — `Recall that unitary matrices satisfy $UU^H=U^HU=I$ so they are normal and as a result are unitarily diagonalizable. Furthremore note that all of their eigenvalues have magniture one:`
- **numerical_linear_alg/HW5.tex:193** — `for some eigenvector $v$. note that since this was nonzero that means that $|\lambda|^2=1$ so they all have absolute magnitude one. as a result let each eigenvalue be $\lambda_j$ note that we can write this in polar form as $\lambda_j=e^{i \theta_j}$ for some theta since they are magnitude one (these thetas are real angles). then:`
- **numerical_linear_alg/HW5.tex:203** — `Note that earlier we have proven that if A matrix is hermitian positive definite it has a square root. take $\sqrt{A^*A}=S$ namely $V\Sigma V^T$ where $\Sigma$ is the square roots of hte eigenvalues so that $V\Sigma V^TV\Sigma^T V^T=V\Sigma^2V^T$ is the eigenvalue decomposition (we can do this since $A^*A$ is positive semidefinite and hermitian, so this square root is also positive semidefinite). Note this is also hermitian. but note that V is literally the svd right singular vectors of A so take:`
- **numerical_linear_alg/HW5.tex:207** — `now note that if we took the full svd of A then $U,V$ are both unitary so $UV^T$ is also unitary. By part one we can write this as $e^{i\Theta}=UV^T$ so then:`
- **numerical_linear_alg/HW5.tex:240** — `note that $V^T$ is an $r\times n$ matrix with orthonormal rows so $V^TV$ is $r\times r$ identity:`
- **numerical_linear_alg/HW5.tex:242** — `from here note that $U$ is an $m\times r$ matrx with orthonormal collumns so $U^TU$ is the identity $r\times r$:`
- **numerical_linear_alg/HW5.tex:311** — `With this problem I loaded in all of the images and stacked their flattened versions into a matrix. I then took the svd like in the previous problem and kept only the first k nonsingular values before multiplying hte matrix back together. Note that in this case it was really important that I computed the reduced svd in numpy so I didn't crach my computer.`
- **numerical_linear_alg/HW3.tex:61** — `Note that by problem 4 we know that any matrix is orthonormally similar to an upper triangular matrix with the eigenvalues on the diagonal. So take $A$:`
- **numerical_linear_alg/HW3.tex:65** — `Now note:`
- **numerical_linear_alg/HW3.tex:88** — `to do this take an arbitrary eigenpair $(\lambda,v)$ then note that:`
- **numerical_linear_alg/HW3.tex:98** — `now note that we chose $i$ such that $v_i>v_j$ for any other J this means that $\frac{v_j}{v_i}<1$ thus:`
- **numerical_linear_alg/HW3.tex:114** — `Easy proof: Because we proved it in four we know every matrix is unitarily similar to an upper triangular matrix with the eigenvalues on the diagonal. From here note that if A is skew hermitian:`
- **numerical_linear_alg/HW3.tex:125** — `First of all note that if $\lambda,v$ is an eigenpair of $A$ then:(choosing v to be unit length)`
- **numerical_linear_alg/HW3.tex:137** — `Furthermore take any matrix A. We know that it has at least one eigenvalue since it has a characteristic polynomial. Take that eigenvalue $\lambda_1, v_1$ and corresponding unit eigenvector. construct $Q_1=[v_1,q_2,\dots,q_n]$ then note that:`
- **numerical_linear_alg/HW3.tex:161** — `Note from there that this new matrix $Q_1^*AQ_1$ is also skew hermitian $-A^*=-(Q_1^*AQ_1)^*=-Q_1^*A^*Q_1=Q_1^*(-(-A))Q_1=Q_1^*AQ_1$. Thius this lower block $A_1$ is also skew hermitian. and the upper right part must be zero:`
- **numerical_linear_alg/HW3.tex:176** — `Furthermore we can repeat this process again. Note that $A_1$ thus has at least one eigenpair $v_2,\lambda_2$ construct an orthonormal basis $U_2=[v_2,z_2,\dots,z_{n-1}]\in \R^{(n-1)\times (n-1)}$`
- **numerical_linear_alg/HW3.tex:229** — `To prove this take any matrix A. Note that A has at least one eigenpair $\lambda_1, v_1$ because the characteristic polynomial has at least one root. construct $Q_1=[v_1,q_2,\dots, q_n]$ where we complete $v_1$ to an orthonormal basis $q_2,\dots,q_n$`
- **numerical_linear_alg/HW3.tex:261** — `We can then note that $A_1$ also has at least one eigenpair by the same argument as before. Call this $\lambda_2,v_2$. Complete $v_2$ to an orthonormal basis of $\R^{(n-1)\times (n-1)}$.`
- **numerical_linear_alg/HW3.tex:275** — `From there note that:`
- **numerical_linear_alg/HW3.tex:332** — `From here note that since eigenvalues are invariant under unitary transformation ($U^*AU(U^*v)=U^*Av=U^*\lambda v=\lambda U^*v$, so any eigenvalue $\lambda$ of A with eigenvector $v$ is also a eigenvalue of this new matrix with eigenvector $U^*v$). The eigenvalues of A are the eigenvalues of $T$ which we can just read off of the diagonal.`
- **numerical_linear_alg/HW3.tex:338** — `a) To show this first note that $\sup |W(A)|=\sup_{x\neq 0}|\frac{\langle Ax,x\rangle}{\norm{x}^2}|$ from here clearly note that:`
- **numerical_linear_alg/HW3.tex:350** — `So the first inequality is true furthremore note that by cuachy shwartz:`
- **numerical_linear_alg/HW3.tex:359** — `b) so note that W is a set function so we will view how this operates on arbitrary object in the set. Let $a\in W(e^{i \theta}A)$ that means $a=\frac{\langle v, e^{i\theta}Av\rangle}{\norm{v}^2}$ for some v. Which mean:`
- **numerical_linear_alg/HW3.tex:402** — `% TODO: This technically traces out a much larger shape`
- **numerical_linear_alg/diagonalizabilty.md:124** — `Note that if A is hermitian then the numerical range is literally just a thing on the real line. Suppose that $||x||=1$ then $R_A(x)=x^*Ax=x^*U^*\Lambda Ux$ define $c=Ux$ then $R_A(x)=c^*\Lambda c=\sum \lambda_j |c_j|^2$ so this is always a real number. Order that $\lambda_1<\lambda_2<\dots\leq \lambda_n$ then that means that the raleigh quotient is a convex combination of things. so they are always greater than the smallest and larger than the greatest:`
- **numerical_linear_alg/HW4.tex:86** — `Note I left off the last n-1 entries of the vector because we will not be using them.`
- **numerical_linear_alg/HW4.tex:88** — `Now note that since these two must be equal we know that $\sum |T_{1j}|^2=|T_{11}|^2$. Thus $T_{1j}=0$ for $j\neq 1$. From this we immidiately get equality above.`
- **numerical_linear_alg/HW4.tex:134** — `Then note that:`
- **numerical_linear_alg/HW4.tex:139** — `from here note that this is the eigenvalue decomposition of $A^*A$ and $\Lambda*=\Lambda$ because all of the eigenvalues are real. Then note that the singular values are:`
- **numerical_linear_alg/HW4.tex:162** — `Because every matrix has an singular value decomposition. Note that $\Sigma^*=\Sigma$ since they are all real and positive. Also note that $V^*V=I$ so:`
- **numerical_linear_alg/HW4.tex:192** — `And remember that the two norm of a matrix is the largest singular value (I think we proved this but if not note that since the two norm is invariant under unitary transformation $\norm{A}=\norm{\Sigma}$ and the norm of that diagonal (even if rectangular) matrix is just the largest entry on the diagonal). so`
- **numerical_linear_alg/HW4.tex:248** — `Here can use a cheap trick note:`
- **numerical_linear_alg/HW4.tex:253** — `Note that if we convert this into the $\sum ||(I-P_V)a_j+P_Va_j||_2^2$ we can apply pythagoras to each element in turn and then convert back to get:`
- **numerical_linear_alg/HW3.log:265** — `\OT1/cmr/m/n/12 From here note that since eigen-val-ues are in-vari-ant un-der uni-tary trans-for-ma-tion ($\OML/cmm/m/it/12 U[]AU\OT1/cmr/m/n/12 (\OML/cmm/m/it/12 U[]v\OT1/cmr/m/n/12 ) =`
- **numerical_linear_alg/HW1.tex:15** — `% looks normal.  Note that 1.1=1/.9090909...`
- **numerical_linear_alg/HW1.tex:71** — `From here note that $R_{k,:}$ is just the kth row of R and $C_{:,l}$ is merely the lth collumn of C. Thus we are just taking an inner product here between the kth row of R and the lth column of C`
- **numerical_linear_alg/HW1.tex:78** — `b) to do this we follow the definition note that:`
- **numerical_linear_alg/HW1.tex:122** — `note that since A is invertible $Ax=0$ iff $x=0$ thus we know that if $x\neq 0,Ax=y\neq 0$:`
- **numerical_linear_alg/HW1.tex:140** — `First note that`
- **numerical_linear_alg/HW1.tex:146** — `Now note that:`
- **numerical_linear_alg/HW1.tex:154** — `For the c inequality choose $x=e_1$ Note that $\norm{e_1}_1=1$ and $\norm{e_1}_2=\sqrt{1+0+0+\dots}=1$, thus $\norm{x}_1=\norm{x}_2$`
- **numerical_linear_alg/HW1.tex:166** — `Note that since we need to take a supremum over all possible x values we can pick an x that achieves this bound namely $e_k$ where k corresponds to the largest collumn sum thus:`
- **numerical_linear_alg/HW1.tex:171** — `To prove the infinity norm statement note that:`
- **numerical_linear_alg/HW1.tex:192** — `To prove this take the definition of the induced norm (Note let $A\in \R^{m\times k}, B\in \R^{k\times n}$)`
- **numerical_linear_alg/HW1.tex:206** — `For the frobenius norm note that:`
- **numerical_linear_alg/HW2.tex:15** — `% looks normal.  Note that 1.1=1/.9090909...`
- **numerical_linear_alg/HW2.tex:67** — `So $Ab_k=e_k$. From this note that because of this we have $(Ab_k)_i=\sum_{j=1}^{i}A_{ij}(b_k)_j=0$  For $i< k$ (Note that since A is lower triangular we only sum up to i). In particular if $i=1<k$ then:`
- **numerical_linear_alg/HW2.tex:160** — `To prove this Assume the the projector is hermitian then, Note that $P$ projects to the range and $I-P$ projects to the null space. We show that any two vectors in this are orthogonal`
- **numerical_linear_alg/HW2.tex:168** — `To prove the other direction. Assume that the range and null space are orthogonal. construct and orthonormal basis for the range and null space note that since the dimension of range and null space add up to the dimension of the whole space (and they are orthogonal by assumption) then this consitutes an orthonormal basis for the whole space`
- **numerical_linear_alg/HW2.tex:172** — `From this note that if a vector $q_j$ is in the range of P then:`
- **numerical_linear_alg/HW2.tex:181** — `call this matrix Q then note that (if $q_k$) is in the range subseciton`
- **numerical_linear_alg/HW2.tex:197** — `So P is thus hermitian since $P^*=(Q_kQ_k^*)^*=Q_kQ_k^*=P$. (Note that here $Q_k$ is Q excluding the last $k+1,n$ collumns).`
- **numerical_linear_alg/HW2.tex:204** — `As an aside. From this note that if a vector $v$ is in the range of any projection P then:`
- **numerical_linear_alg/HW2.tex:215** — `Take some artbirary vector x. Note that sicne the space $\R^n$ is a direct sum of the range and null space we can write $x=v+w$ where $v\in$ the range and $w\in$ null space specified earlier.`
- **numerical_linear_alg/HW2.tex:217** — `then note that:`
- **numerical_linear_alg/HW2.tex:246** — `Now note that if $w^\star v=0$ then $v-u(w^\star v)=0$ a contradiction. so $w^\star v\neq 0$. and as a result`
- **numerical_linear_alg/HW2.tex:261** — `Note that $(-(I+uw^\star)^{-1}u)=v$ is a vector so $K=vw^\star$ so it is rank one`
- **numerical_linear_alg/HW2.tex:290** — `Note that since A is invertible $A+uw^*$ is invertibel iff $(I+A^{-1}uw^*)$ is invertible. Thus by a previous part this is invertible iff $w^*(A^{-1}u)\neq -1$ (Since this is a rank one pertubation of the identity)`
- **numerical_linear_alg/HW2.tex:311** — `Note that`
- **numerical_linear_alg/HW2.tex:366** — `Construct a basis for the range of $P$ call it $q_1,\dots, q_k$ and a basis for the null space of $q_{k+1},\dots,q_n$. Note that putting these two basis together constructs a basis for the whole space (however this is not necessarily a unitary basis) by the rank nullity theorem.`
- **numerical_linear_alg/HW2.tex:368** — `From this note that if a vector $q_j$ is in the range of P then:`
- **numerical_linear_alg/HW2.tex:428** — `Where the lower case v in this case refers to entries of $V_A$ and the $\lambda_i$ refers to eigenvalues of A.. Note that`
- **numerical_linear_alg/HW2.tex:430** — `Now note that since each $v_{:,j}$ is an eigenvector of A with corresponding eigenvalue $\lambda_j$`

## numerical_linear_alg/6610 (2)/6610

- **numerical_linear_alg/6610 (2)/6610/HW5.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...`
- **numerical_linear_alg/6610 (2)/6610/HW5.tex:76** — `So $\lambda D+\lambda L+U$ is singular. Note that a diagonally dominant matrix cannot be singular. If $\lambda =1$ then this is just A which means its diagonally dominant thus we have a contradiction. Similarly for any $\lambda >1$ we have this being diagonally dominant so it is singular. Thus we must have $\lambda < 1$`
- **numerical_linear_alg/6610 (2)/6610/HW5.tex:97** — `note that`
- **numerical_linear_alg/6610 (2)/6610/HW4.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...`
- **numerical_linear_alg/6610 (2)/6610/HW4.tex:74** — `Note that we can pass the norm through because the series converges absolutley`
- **numerical_linear_alg/6610 (2)/6610/HW4.tex:101** — `Note that:`
- **numerical_linear_alg/6610 (2)/6610/HW4.tex:191** — `note that`
- **numerical_linear_alg/6610 (2)/6610/HW_3.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...`
- **numerical_linear_alg/6610 (2)/6610/HW_3.tex:143** — `To prove this note that we can write A:`
- **numerical_linear_alg/6610 (2)/6610/HW_3.tex:164** — `To show this first part. Note that since we have more columns than rows we know that $n-m$ of the columns can be formed by linear combinations of the first m columns. We`
- **numerical_linear_alg/6610 (2)/6610/HW_3.tex:166** — `Perhaps we should do this using QR note that the QR factorization will looks like:`
- **numerical_linear_alg/6610 (2)/6610/HW_3.tex:174** — `Note that the last $n-m$ cols of r will all be zero because we can form them as linear combinations of the first m collumns in the gram schmidt process.`
- **numerical_linear_alg/6610 (2)/6610/HW_1.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...`
- **numerical_linear_alg/6610 (2)/6610/HW_1.tex:63** — `Note that since this is unitary we know thatthe inner product of the first row and first collumn is 1 while the inner product of the first row and ith collumn is zero. For this first statement to be true we know that $a_{11}=1/\bar{a_{11}}$. For the second statement this can only be true if the collumn below $a_{11}$ is all zero (to cancel out to zero).`
- **numerical_linear_alg/6610 (2)/6610/HW_1.tex:111** — `To prove this note that:`
- **numerical_linear_alg/6610 (2)/6610/HW_2.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...`
- **numerical_linear_alg/6610 (2)/6610/HW_2.tex:77** — `Note then that:`
- **numerical_linear_alg/6610 (2)/6610/HW_2.tex:86** — `We need to find an eigenvalue decomposition note:`
- **numerical_linear_alg/6610 (2)/6610/HW_2.tex:110** — `Now note that`
- **numerical_linear_alg/6610 (2)/6610/HW_2.tex:124** — `To prove this note that`

## numerical_linear_alg/Math6610NumericalAnalysisI

- **numerical_linear_alg/Math6610NumericalAnalysisI/Math6610-lecturenotes-Sept21-Oct052022.pdf:95090** — `mR8բL4PF:!b	ToDO+/8+g }lqHdr\@{Gw6eX7NS(r܆5Ss6~K`
- **numerical_linear_alg/Math6610NumericalAnalysisI/Math6610-lecturenotes-Sept30-Oct052022.pdf:19473** — `mR8բL4PF:!b	ToDO+/8+g }lqHdr\@{Gw6eX7NS(r܆5Ss6~K`
- **numerical_linear_alg/Math6610NumericalAnalysisI/Math6610-lecturenotes-Nov082022.pdf:13826** — `үŀtodO@ƪN%x4<G1tTV1`

## numerical_linear_alg/Review

- **numerical_linear_alg/Review/review.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...`
- **numerical_linear_alg/Review/notes.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...`
- **numerical_linear_alg/Review/notes.tex:62** — `So to prove the thing with matrix splits. Assume that a matrix A is irreducibly diagonally dominant. Note then that at least one row in`
- **numerical_linear_alg/Review/notes.tex:77** — `Let A be a full ranke matrix. Let B be some rank r matrix. Let $A_r$ be the rank r approximation to A. Note that if we take one of the first $r+1$ right singular vectors of eA tn because B is only rank r we know that at least one of them lies in the null space of b. Call it index j. We will take the supremum over all unit vectors x`
- **numerical_linear_alg/Review/notes.tex:113** — `From this we knwo that $UL^{-1}$ is unitary. However note that it is also upper triangular. That means that it is actually diagonal and that the diagonal entries must be the roots of unity. From the fact that we know that the diagonal entries of U are real and positive, we also know that the diagonal entries of $L^{-1}$ are real and positive. Thus they must be one. so:`

## numerical_odes

- **numerical_odes/LeVeque_heat.ipynb:24** — `"note that for $U_1,U_{m}$ then:\n",`
- **numerical_odes/LeVeque_heat.ipynb:96** — `"We next note that in the two norm that eigenvectors of this operator correspond to eigenvectors of the derivative operator evaluated at the grid points:\n"`
- **numerical_odes/LeVeque_heat.ipynb:278** — `"note that even if we disectrize:\n",`
- **numerical_odes/numerical_odes.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...`
- **numerical_odes/numerical_odes.tex:60** — `Assume that $f\in C^{(n+1)}(\R)$ then note that:`
- **numerical_odes/numerical_odes.tex:169** — `Where $g$ is our approximation to the second order derivative. Typically when deriving this we only care about the big-O and what order it is (say $O(h^p)$) and we say that $\tau_j=O(h^p)$. Note that in this definition we assume we know u and expand each taylor series on u not $U$`
- **numerical_odes/numerical_odes.tex:201** — `Note that then if f is a discrete sum of delta functions that the solution to the BVP is then:`

## numerical_odes/6620 (2)/6620

- **numerical_odes/6620 (2)/6620/HWHW 3.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...`
- **numerical_odes/6620 (2)/6620/HWHW 3.tex:67** — `Ok So the idea here is we want to use a taylor expansion. Note that if we just have two points then they think:`
- **numerical_odes/6620 (2)/6620/HWHW 3.tex:151** — `note that`
- **numerical_odes/6620 (2)/6620/HW5.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...`
- **numerical_odes/6620 (2)/6620/HW5.tex:82** — `note that`
- **numerical_odes/6620 (2)/6620/HW4.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...`
- **numerical_odes/6620 (2)/6620/HW4.tex:143** — `note that`
- **numerical_odes/6620 (2)/6620/HW_1.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...`
- **numerical_odes/6620 (2)/6620/HW_2.tex:14** — `% looks normal.  Note that 1.1=1/.9090909...`
- **numerical_odes/6620 (2)/6620/HW_2.tex:113** — `To prove it is odd. Note that this polynomial is p. Define $q(x)=-p(-x)$. Note that Q also interpolates the data. Because q is also of the same degree as p and interpolates the data they must be equal. so $p(x)=-p(-x)$`
- **numerical_odes/6620 (2)/6620/HW_2.tex:119** — `Note the lagrange basis functions are unique in that they satisfy $l_j(x_j)=1$ for each $x_j$. and zero on the other ones. Suppose you interpolate $1$ then we know that:`

## odes

- **odes/reading_week2.md:33** — `Note that we can often transform equations bty using an appropriate change of variables. When you do this take a new variable $y=f(x,t)$ and then just differentiate through this using the chain rule`
- **odes/day_2.md:18** — `Note that this is a second order ode. We want to convert this to a first order system`
- **odes/day_2.md:83** — `now note that both zeros depend on H, for $H< \frac{\gamma k}{4}$ there are two positive fixed points where $r(10 \frac{N}{k})-H=0,\implies N\pm = \frac{(r\pm \sqrt r^2-\frac{4Hr}{k} )k}{2r} $`
- **odes/day_2.md:111** — `Note that one solution is definitely $x=0$. Another could definitely be $\frac{dx}{x^{1/3}}=dt$`
- **odes/day_2.md:117** — `We need to think about this till after class. Note the solutions are just piece wise connections of our two solutions.`
- **odes/existence.md:26** — `<!-- NOTE: Remark we can pass limits inside continuous functions -->`
- **odes/existence.md:28** — `<!-- NOTE: Gronwalls says that: -->`
- **odes/existence.md:32** — `<!-- NOTE: What are the assumptions on Gronwalls? -->`
- **odes/stability_10.md:69** — `<!-- NOTE: This may be on the exam -->`
- **odes/stability_10.md:82** — `for some set of jordan blocks $J$ from here note tjhat:`
- **odes/stability_10.md:104** — `For the final case we will note that we can no longer bound the nilpotent matrix by an exponential. However since there are no exponentials anywhere (The norm of the matrix is just one). We can bound it by  a polynomial instead.`
- **odes/stability_10.md:191** — `<!-- NOTE: This will be on the exam -->`
- **odes/day_5.md:64** — `To prove this. Note that if the solution is ever a or b, then it will always stay at one of those, so by the previous lemma since they can't intersect. So for $x_0\in (a,b)$ the solution never reaches either of those.`
- **odes/HW3.tex:61** — `% NOTE: ONE OF THESE WILL Be on the quals`
- **odes/HW3.tex:71** — `% NOTE: Note that when proving things with this remember to start with the derivativeof the invariant set function applied to the flow map`
- **odes/HW3.tex:84** — `From here note that because f is continuous on a bounded domain then we can bound it above by some $|f|<M$. Similarly for $|\nabla g|<K$ so:`
- **odes/HW3.tex:89** — `Note that because $g(\phi_t(x))$ is small it is well approximated by a taylor  series around $x_b$ $\nabla g(\phi_t(x))\approx \nabla g(x_b)+D^2g(x_b)(\phi_t(x)-x_b)+h(\phi_t(x))(\phi_t(x)-x_b))$ note that because we are considering small $g$ we will have that $\phi_t(x)$ is close to $x_b$. From this since the peano form of the remainder approaches zero when that exact thing happens. we can choose a sufficiently small radius so that $h_(\phi_t(x))<\epsilon$  So we can plug that into our equations:`
- **odes/HW3.tex:94** — `Note that because g is smooth then this $D^2g(x_b)$ is also bounded call this bound $N=D^2g(x_b)+\epsilon$:`
- **odes/HW3.tex:96** — `\textbf{Remark}: Above we used a taylor series expansion to bound $|\nabla g(\phi_t(x))-\nabla g(x_b)|$ however one could also note that smooth functions on bounded sets are also lipshitz so then it immideiately follows that:`
- **odes/HW3.tex:97** — `$|\nabla g(\phi_t(x))-\nabla g(x_b)|\leq N(\phi_t(x)-x_b)$. On a similar note I could have noted that since $\nabla g$ is lipshitz continuous on the bounded domain, then the dot product of two lipshitz functions on a bounded domain is also lipshitz. Then I could have just take $|\frac{d}{dt}g(\phi_t(x))|=|Dg(\phi_t(x))f(t,\phi_t(x))|=|Dg(\phi_t(x))f(t,\phi_t(x))-Dg(x_b)f(t,x_b)|\leq L|\phi_t(x)-x_b|$ for some constant L. Things are a lot quicker in retrospect. But either way, we go back to the main argument!`
- **odes/HW3.tex:110** — `Note from here that this distance $|\phi_t(x)-x_b|$ is literally the definition of $g$ as the signed distance (note that its an absolute value, but we will only consider $\phi_t(x)$ that is inside or on the boundary so this is eqivalent to the signed distance). We take r small enough so $x_b$ is the unique closest point is the unique closest point.`
- **odes/HW3.tex:146** — `b) For this part assume that we start inside the set $U$. Note that if we never approach the border then clearly our solution is invariant. However if it does approach the border all of the problems will always occur near the border because our solution is continuous. By the intermediate value theorem if it were to leave our set it would have to get near the border first. For this reason without loss of generality we consider a $x_0$ close enough to the border so our previous theorem applies. thus:`
- **odes/HW3.tex:152** — `c) For the firs part note that at time zero (if $x_0\in \partial U$):`
- **odes/HW3.tex:156** — `Note that because we are doing time $t=0$ I just plugged in $\phi_0(x_0)=x_0$`
- **odes/HW3.tex:185** — `(Using the same notation in the slides were we are taking the derivative at the point A in the direction of B $\det'(A)(B)$). (Note that the inverse here exists because we proved it in class)`
- **odes/HW3.tex:204** — `% NOTE: remember the derivative of the determinant`
- **odes/HW3.tex:212** — `% NOTE: Memorize this bound`
- **odes/HW3.tex:213** — `First note that because all of the eigenvalues of A are distinct and have negative real part then we can bound $e^{At}$ by:`
- **odes/HW3.tex:229** — `Note that for each j $|e^{\lambda_j t}|= e^{\text{real}(\lambda) t}$`
- **odes/HW3.tex:247** — `First note that the first term abtrarily approaches zero because of the bound on the exponential.`
- **odes/HW3.tex:249** — `From here note that because $|g(s)|\rightarrow 0$ there is a time l when $s>l$ means $g(s)<\epsilon$ then:`
- **odes/HW3.tex:257** — `Note that because $g(s)$ is continuous it is bounded over this compact interval say by M:`
- **odes/HW3.tex:273** — `Note that we can always choose l to make epsilon as small as we like. So choose an arbitrarily small epsilon and we will get a corresponding finite l. Since l is still finite then the given exponentials will still approach zero after enough time.`
- **odes/HW3.tex:301** — `% NOTE: Remember The advanced gronwall`
- **odes/HW3.tex:308** — `Where $e^{\Lambda}$ is applied elementwise on the matrix and $u_j$ are the rows of $V^{-1}$. Note that each of these terms approach zero because they each have a negative exponential. The rate of convergence is just the eigenvalue with real part closest to zero (further to the right on the complex plane) because that will decay the slowest. This first one only relies on initial data for the coeffients of the exponentials so how high they start before they start decaying.`
- **odes/HW3.tex:387** — `Note that the norm of that diagonal matrix is the eigenvalue with the largest real part which i denote $\lambda_j$. So thus it is proven.`
- **odes/HW4.tex:155** — `Note that I just did the jordan form matrix exponential in my head (its just a polynomial). Combining all of these together we get:`
- **odes/HW4.tex:277** — `Finally if $\rho^2=4\omega^2$. Then we will have to use the generalize eigenspace because we will have a degenerate eigenvalue at $-\rho/2$. to do this first note that one eigenvector remains the same $% 2 x 1 BMatrix`
- **odes/week1.md:11** — `For energy, first multiply by $\dot x$ from the rest. Then isolate the $\dot x^2$ term from the rest. This enables us to use positivity. We then can use integrating factors on the other side to better under stand things. note we will usually have a $\frac{d}{dt}(\dot x/2)^2=\ddot x\dot x$ term as well as a`
- **odes/non-autonomous_11.md:27** — `Note that $\Phi(t)$ maps the point from the initial condition to its position at time t. So then $\Phi(t_0)$ maps from the point it is at at zero to its point at $t_0$ whereas the inverse maps $t_0$ to its point at the initial condition.`
- **odes/matrix_exponentials_9.md:33** — `Let $Q=[\text{re}(v),\text{im}(b)]$ note that we can express $v, \overline{v}$ interms of these:`
- **odes/matrix_exponentials_9.md:38** — `now note that $\lambda = \rho + i\omega, v= re(v)+i im(v)$`
- **odes/flowmaps.md:34** — `Note that we can do this because its globally lipshitz`
- **odes/flowmaps.md:83** — `note that the solution is:`
- **odes/flowmaps.md:127** — `<!-- NOTE: This will be in the exam -->`
- **odes/HW2.tex:15** — `% looks normal.  Note that 1.1=1/.9090909...`
- **odes/HW2.tex:60** — `Note for this problem we want to find the Lipshitz bound L. This is the same as bounding the norm of the derivative with respect to mu. Then take:`
- **odes/HW2.tex:89** — `Alternatively you can do a different method with derivative tricks, note this is not my main answer but is included for completeness.`
- **odes/HW2.tex:91** — `For this problem note that we can write the integral form:`
- **odes/HW2.tex:154** — `% NOTE: From this firstr problem. I learned that if I have multiple components I can use the triangle inequality first to separate them. Then use the multivariate calculus trick, Then gronwalls advanced inequality.`
- **odes/HW2.tex:156** — `% NOTE: from the second problem. just follow proofs through`
- **odes/HW2.tex:188** — `Now note that becaue $p$ is increasing $\frac{1}{p}$ is decreasing. As a result $\int_0^\frac{h}{2}\frac{1}{p(s)}\geq \int_\frac{h}{2}^h \frac{1}{p(s)}$. From this we can gather that`
- **odes/HW2.tex:194** — `From here note that the inequality we have derived`
- **odes/HW2.tex:220** — `Note that for small $u(t)$ $|\log(u(t))|=-\log(u(t))$ for $|u(t)|<1$ while for $u(t)>1$ it is $\log(u(t))$. Furtherome not that because $\rho$ is positive and increasing we have that $u(t)$ is strictly increasing. (It is a positive number plus the integral of a positive number)`
- **odes/HW2.tex:236** — `Here is a graph of the normal lipshitz bound $e^{Lt}|x_0-y_0|$ in red verses the new bound $e^{e^{Lt}\frac{1}{1-\log(|x_0-y_0|))}-1}$ in blue. You can see that the new bound grows way faster! This can be seen in the equation just because we will have an exponential to a positive exponential (because $\frac{1}{1-\log(|x_0-y_0|)}>0$ in this case). Note for the graph I set $x_0=0,y_0=0.1,L=1$`
- **odes/HW2.tex:267** — `Here is a graph of the normal lipshitz bound $e^{Lt}|x_0-y_0|$ in red verses the new bound $e^{e^{Lt}(1+\log|x_0-y_0|)-1} $ in blue. You can see that the new bound grows way faster! This can be seen in the equation just because we will have an exponential to a positive exponential (because $1+\log(|x_0-y_0|)>0$ in this case). Note for the graph I set $x_0=0,y_0=1.1,L=1$`
- **odes/floquet_12-13.md:34** — `Let $\Phi(t)$ be the fundamental matrix solution note:`
- **odes/floquet_12-13.md:43** — `First note that M is invertible. Secondly note the previous equality`
- **odes/floquet_12-13.md:67** — `First note that we have the following relationship:`
- **odes/floquet_12-13.md:71** — `This implies that $\chi(t+kT)=\mu_j^k\chi_j(t)$. Note this either diverges to infinity or converges to zero.`
- **odes/floquet_12-13.md:98** — `note chi could be complex but he said to ignore that for now because it will cancel out later. This also doesn't quite work but he says it will work out. if this is real then this works for a period of 2T because the angle will just be -1 so two of them will be 1.`

## odes/volume_3_textbook

- **odes/volume_3_textbook/V3Ch11-W2024.pdf:22037** — `G6uټL@z9Jǂim'X'.*Wε}Of<,	R	lOODr#	σdOU'z)rc<5%~yWH*`jԱr}y˂Iqle{&L'Xvh3^M|u\m뼜镚l'XwV%T<_e;|.>:-vuqĪ>.]߳i_1ͤF.^todo-O2u-1]P4Z@tyAk[^6[[U<lXG>!}1xV+FXYB?MȈNԗ}D.nb&iGc`L>_E.Vl'W+T|;0G69v H>zߩyOM[ލAڿ	?7@;/Ai6ĄyfK8ÊAjO"Ʒٷ!s\?|EMZ=y*C;\H\>`$|@V;OkW!`5nCkI6Ǵ&7o.Ax4_=7)i]|>£	3x@O@sGqBQTL~`

