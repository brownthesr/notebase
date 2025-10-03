# Generative Modeling

Likelihood models are not great because they maximize the elbo which is a surrogate objective. Implicit models often require adversarial training and lead to mode collapse and instabilities.

## VAE Likelihood modeling

So our goal is to be able to find a set of parameters that maximize:
$$\begin{align}
p(x|\theta)
\end{align}$$
this is maximum likelihood modeling. In this we will just call this $p_ \theta(x)$. This is equivalent to maximizing the log of this:

$$\begin{align}
\log(p_ \theta(x))=\log( \mathbb{E}_{q(z|x)}[\frac{p_ \theta(x,z)}{q(z|x)}])\geq \mathbb{E}_{q(z|x)}[\log \frac{p_ \theta(x,z)}{q(z|x)}]
\end{align}$$
this is true. We can then expand things:
$$\begin{align}
= \mathbb{E}_{q(z|x)}\log p_ \theta(x,z)-\log q(z|x)\\
= \mathbb{E}_{q(z|x)}\log p_ \theta(x|z)+\log(p(z))-\log q(z|x)\\
= \mathbb{E}_{q(z|x)}\log p_ \theta(x|z)-D_{KL}( q(z|x)||p(z))\\
\end{align}$$
we want to maximize this in the hopes of maximizing the log likelihood. This is equivalent to minimizing the above objective which is what we typically train neural nets to do.

So what we do is we first have an encoder take in the image (or data) and output a mean and a variance(usually this is the log of the variance so it can be negative or positive). This gives a distribution $q_\theta(z|x)=\mu_\theta(x),\sigma^2_\theta(x)$. From this we use the re parameterization trick to sample from a unit gaussian $\epsilon$ and take a sample from this new guy $z=\mu+\sigma\cdot \epsilon$

The decoder the takes in this re parameterized $z$ and outputs the means and variance of our desired image (again by log of variance). Assuming this is a gaussian we can reduce the first term in the ELBO (note the expectation is approximated by taking many samples).
$$\begin{align}
\log(p_ \theta(x|z)) = \frac{-1}{2\sigma^2||x-\mu_\theta(z)||^2-\frac{D}{2}\log(2\pi \sigma^2)
\end{align}$$
where $D$ is the dimension.

We can then compute the loss for the KL analytically. If we choose $p(z)=N(0,I)$ then:
$$\begin{align}
KL(q_\theta||p)=\frac{1}{2}\sum_j^d (\mu_j^2+\sigma^2_j-1-\log \sigma_j^2)
\end{align}$$
we then combine these losses for a minibatch (funnily enough we usually only sample one z per data point). We then run Adam on this.

## Implicit models (GANs)
We don't explicitely learn a distribution we just train a decoder.

## Score based model

We assume our pdf that we want to maximize is:
$$\begin{align}
p_\theta(x)=\frac{e^{-f_ \theta(x)}}{z_\theta}
\end{align}$$
Where we have this nasty normalizing constant.

Once again we can train such a model by maximizing the log of this likelihood:
$$\begin{align}
-f_ \theta(x) - \log z_\theta
\end{align}$$
but this normalizing quantity will most likely be awful to compute. Likelihood models typically either restrict their models to compute these analytically or approximate it (VAE or MCMC, since we lower bound things)

By modeling the gradient of this (with respect to x). we are able to completely ignore the second term to get:
$$\begin{align}
s_\theta (x)=-\nabla_x f_ \theta(x)
\end{align}$$
We can then train a model to minimize the fisher divergence:
$$\begin{align}
\mathbb{E}_{p(x)}[||\nabla_x \log p(x)-s_ \theta(x)||^2]
\end{align}$$
so the squared $l^2$ distance. However we do not know the ground truth score. There are multiple methods of estimating this
<!-- TODO: Research methods for approximating scores! -->

### Langevin Dynamics
Once we have the score function:
$$\begin{align}
s_ \theta(x)\approx \nabla_x \log p(x)
\end{align}$$
we can use MCMC to sample from the distribution (specifically langevin dynamics). If we start from any arbitrary entire distribution we can obtain:
$$\begin{align}
x_{i+1}=x_i+\epsilon s_ \theta(x_i)+\sqrt{2\epsilon}z_i
\end{align}$$
where $z_i\sim \mathcal{N}(0,1)$. As $\epsilon\rightarrow 0,K\rightarrow\infty$ then this will approximate a sample from $p(x)$ (see ACME)

The issue with Langevin dynamics is that it is only accurate in high density regions (where our model is trained) but it is highly likely we will not be in those regions.

#### Multiple noise perturbations (Annealed MCMC)
To avoid this its possible to perturb the initial data so that we have more representation in low volume regions. But we don't want to perturb it too much or we will lose the original distribution. So to accomplish this a variety of papers have proposed adding multiple levels of noise perturbations $\sigma_1,\dots, \sigma_n$. The noise perturbations are just obtained by convolving our original distribution with a gaussian of variance $\sigma_i^2$ and mean 0.

It is easy to sample from this distribution just sample from $x\sim p(x)$ and then take $x+\sigma_i z, z\sim \mathcal{N}(0,1)$. They then train a neural network to match the score of each different noise level:
$$\begin{align}
s_{\theta}(x,i)\approx \nabla_x \log(p_{\sigma_i}(x))
\end{align}$$
The training objective for this neural net is a weighted combination of the fisher ddivergences
$$\begin{align}
\sum_i \lambda(i)\mathbb{E}_{p_{\sigma_i}(x)}[||\nabla_x \log p_{\sigma_i}(x)-s_ \theta(x,i)||^2]
\end{align}$$
Where $\lambda(i)$ weights each noise level. typically this is chosen $\lambda(i)=\sigma_i^2$.

One can then once again run langevin dynamics but at decreasing noise scales. So first doing it at the largest one, then the second largest one, then the third and so one. This is also called Annealed Langevin Dynamics.
### SDEs
Typically one (as you know drake) can represent a Stochastic process with and SDE. Typically with a drift term $f$ and diffusion coefficient $g$
$$\begin{align}
dX=f(X,t)dt+g(t)dW
\end{align}$$
Note that at any time $t$ there is a corresponding distribution of paths at that time $p_t(x)$.

From here note that every SDE has a corresponding reverse SDE that can be solved in reverse to get the original distribution:
$$\begin{align}
dX=[f(X,t)-g^2(t) \nabla_x\log(p_t(X))]dt+g(t)dW
\end{align}$$
Where this is run backwards. The idea here is that we just need to compute the score function at any time $t$ and we are great! (we also need to know the terminal distribution so we can sample something to start with)

The training objective is then the natural extension from above
$$\begin{align}
\int \lambda(t)\mathbb{E}_{p_{t}(x)}[||\nabla_x \log p_{t}(x)-s_ \theta(x,t)||^2]dt\\
\mathbb{E}_{\mathcal{U}[0,T]}\mathbb{E}_{p_{t}(x)}[||\nabla_x \log p_{t}(x)-s_ \theta(x,t)||^2]
\end{align}$$
Where $\lambda(t)$ is a positive weighting function. typically they choose it to be proportional to $\frac{1}{\mathbb E [||\nabla_x \log p(x(t)|x(0))||^2]}$. To balance things.

Note in the neural network itself we typically encode time as a gaussian random feature. namely draw $\omega\sim \mathcal{N}(0,I)$ and set $t_E=[\sin(2\pi \omega t);\cos(2\pi \omega t)]$ (You can set the variance of $\omega$ to be larger if you want).

In their specific case they choose $g(t)=\sigma^t$ and $f(x,t)=0$ so $dX=\sigma^tdW$ when sigma is large (in their code 25) or t is large (but we choose $t=1$) we get that the variance of the final distribution is approximately:
$$\begin{align}
\mathcal{N}(0,\frac{1}{2\log(\sigma)}(\sigma^2-1)I)
\end{align}$$
So this is what we end up sampling from.

So the idea is that they take the exact variance at any time t as $\frac{1}{2\log(\sigma)}(\sigma^{2t}-1))$. Then perturb some random data point:
$$\begin{align}
x_t=x_0 +\sigma(t) z
\end{align}$$
where $z$ is drawn from a multivariate standard normal. The conditional score of this guy is just then $\frac{-z}{\sigma(t)}$. So we train on the perturbed datapoint to match this guy.

### More generally
So typically how we want to estimate the score function is we want:
$$\begin{align}
\nabla_x\log p_t(x)
\end{align}$$
we can actually write out what $p_t(x)$ is given that we know $x_0$ which we do:
$$\begin{align}
p_t(x)=\int p_{data}(x_0)p(x_t|x_0)dx_0
\end{align}$$
note that we can take the gradient log of this to then obtain:
$$\begin{align}
\nabla_x \log(p_t(x))=\frac{\int p_{\text{data}}\nabla_x p(x_t|x_0)dx_0}{\int p_{\text{data}}(x_0) p(x_t|x_0)dx_0}\\
=\frac{\int p_{\text{data}}p(x_t|x_0)\nabla_x \log p(x_t|x_0)dx_0}{\int p_{\text{data}}(x_0) p(x_t|x_0)dx_0}\\
= \mathbb{E}[\nabla_x \log(p(x_t|x_0))]
\end{align}$$
So we really only need to compute the score of the marginal and take an average of a bunch of those. Note that in general if we have a linear ode (f is linear and g only depends on t) then this will always be a gaussian centered at $x_0$ evaluated at $x_t$. Taking the score of a gaussian is pretty simple. it turns out to be for scalar and multivariate:
$$\begin{align}
\frac{-(x_t-x_0)}{\sigma^2}\\
-\Sigma^{-1}(t)(x_t-\mu(t))
\end{align}$$
Where $\mu(t)$ is the mean at time t.

From here note that if we take a sample $x_0$ in our probability space and we can sample $x_t$ (easy because it will be a gaussian). then we can compute the score and train a neural network. Typically how we do that is we take a data point $x_0$ and randomly select a time $t$. If we know $f(x,t)=Ax$ and $g(t)$ is some covariance matrix. then we can exactly compute the mean and variance of the gaussian at time $t$ if we start at $x_0$ it is:
$$\begin{align}
\mu(t)=\Phi(t,0)x_0\\
\Sigma(t)=\int_0^t\Phi(t,s)g(t)g(t)^T\Phi(t,s)^Tds
\end{align}$$
So after computing these we would take $x_t=\mu(t)+\sqrt{\Sigma(t)}z$ where $z\sim N(0,1)$ and the square root of the matrix here is the cholesky decomposition (We are literally just sampling at some point in the future). This gives us a perturbed x. We then compute the score given above although typically we train to match:
$$\begin{align}
\Sigma^{T/2}(t)s_\theta(x_t,t)-\Sigma^{-1/2}(t)(x_t-m(t))\\
\Sigma^{T/2}(t)s_\theta(x_t,t)-z
\end{align}$$
So we train this and it works quite well. We then compute the expected final distribution (usually of mean zero) given the formula for the covariance above. We sample from this before performing reverse diffusion

The hardest part usually is computing the covariance and mean. Also if things are not linear then we don't necessarily have a gaussian at the end so that would make exact sampling of the perturbed $x_t$ harder since we would have to run the differential equation forward in time.
