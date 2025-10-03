import numpy as np
import tqdm
import matplotlib.pyplot as plt
import torch
import torch.nn as nn

sigma = 2.0


def sample_hollow_square(n_samples=1024, inner=2, outer=3, seed=None):
    """
    Uniformly sample points in 2D from a hollow square region:
    Outer square [-outer, outer]^2 minus inner square [-inner, inner]^2.

    Args:
        n_samples: number of samples to draw
        inner: half-side length of inner square (excluded region)
        outer: half-side length of outer square (included region)
        seed: random seed
    Returns:
        samples: (n_samples, 2) numpy array of points
    """
    rng = np.random.default_rng(seed)
    samples = []

    while len(samples) < n_samples:
        # sample uniformly from outer square
        pts = rng.uniform(-outer, outer, size=(n_samples, 2))
        # mask: exclude those inside the inner square
        mask = np.any(np.abs(pts) > inner, axis=1)
        valid_pts = pts[mask]
        samples.extend(valid_pts.tolist())

    return np.array(samples[:n_samples])


class GaussianFourierProjection(nn.Module):
    """Gaussian random features for encoding time steps."""

    def __init__(self, embed_dim, scale=30.0):
        super().__init__()
        # Randomly sample weights during initialization. These weights are fixed
        # during optimization and are not trainable.
        self.W = nn.Parameter(torch.randn(embed_dim // 2) * scale, requires_grad=False)

    def forward(self, x):
        x_proj = x[:, None] * self.W[None, :] * 2 * np.pi
        return torch.cat([torch.sin(x_proj), torch.cos(x_proj)], dim=-1)


class SquareNet(nn.Module):
    """Converts from gaussian to square."""

    def __init__(self, in_dim, hid_dim):
        super().__init__()
        self.time_embed = GaussianFourierProjection(hid_dim)
        self.space_embed = nn.Linear(in_dim, hid_dim)
        self.bn1 = nn.LayerNorm(hid_dim)
        self.layer_1 = nn.Linear(hid_dim, hid_dim)
        self.bn2 = nn.LayerNorm(hid_dim)
        self.layer_2 = nn.Linear(hid_dim, hid_dim)
        self.bn3 = nn.LayerNorm(hid_dim)
        self.layer_3 = nn.Linear(hid_dim, hid_dim)
        self.bn4 = nn.LayerNorm(hid_dim)
        self.layer_4 = nn.Linear(hid_dim, hid_dim)
        self.bn5 = nn.LayerNorm(hid_dim)
        self.out_layer = nn.Linear(hid_dim, in_dim)

        self.activation = nn.ReLU()

    def forward(self, x, t):
        embed = self.time_embed(t) + self.space_embed(x)
        embed = embed + self.layer_1(self.activation(self.bn1(embed)))
        embed = embed + self.layer_2(self.activation(self.bn2(embed)))
        embed = embed + self.layer_3(self.activation(self.bn3(embed)))
        embed = embed + self.layer_4(self.activation(self.bn4(embed)))
        embed = self.activation(self.bn5(embed))
        return self.out_layer(embed)


def marginal_prob_std(t):
    """Returns the standard deviation of out pertubation"""
    t = torch.tensor(t)
    return torch.sqrt((sigma ** (2 * t) - 1.0) / (2 * np.log(sigma)))


def diff_coeff(t):
    return torch.tensor(sigma**t)


def loss_fn(model, x, eps=1e-5):
    random_t = torch.rand(x.shape[0]) * (1 - eps) + eps
    z = torch.randn_like(x)
    std = marginal_prob_std(random_t)
    perturbed_x = x + std[:, None] * z
    score = model(perturbed_x, random_t)
    loss = torch.mean(torch.sum((score * std[:, None] + z) ** 2))
    return loss


epochs = 10000
lr = 1e-3
model = SquareNet(2, 128)
optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

losses = []
tqdm_epochs = tqdm.trange(epochs)
for epoch in tqdm_epochs:
    optimizer.zero_grad()
    points = torch.Tensor(sample_hollow_square(1024))
    loss = loss_fn(model, points)
    loss.backward()
    optimizer.step()
    losses.append(loss.item())
    tqdm_epochs.set_description("Average Loss: {:5f}".format(loss.item()))

plt.plot(losses)
plt.show()
# Now we want to sample from our given distribution

from matplotlib.animation import FuncAnimation

# ====== Animation Setup ======
with torch.no_grad():
    t = torch.ones(1000)
    x = (
        1
        / 2
        * torch.Tensor([[np.sqrt(2), -np.sqrt(2)], [np.sqrt(2), np.sqrt(2)]])
        @ (torch.Tensor(sample_hollow_square(1000)).T)
    ).T
    # x = torch.randn(1000, 2) * marginal_prob_std(t)[:, None]
    t_range = torch.linspace(1, 1e-5, 1000)
    dt = t_range[0] - t_range[1]

    fig, ax = plt.subplots(figsize=(6, 6))
    scat = ax.scatter(x[:, 0].cpu(), x[:, 1].cpu(), s=5)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_aspect("equal")
    ax.set_title("Reverse SDE Sampling")

    def update(frame):
        global x
        t_step = t_range[frame]
        t_feed = torch.ones(x.shape[0], device=x.device) * t_step
        g = diff_coeff(t_feed)
        mean_x = x + (g**2)[:, None] * model(x, t_feed) * dt
        x = mean_x + torch.sqrt(dt) * g[:, None] * torch.randn_like(x)

        scat.set_offsets(x.cpu().numpy())
        ax.set_title(f"Reverse SDE Sampling — t = {t_step:.4f}")
        return (scat,)

    anim = FuncAnimation(fig, update, frames=len(t_range), interval=30, blit=True)

    anim.save("reverse_sde_2.mp4", fps=90, dpi=150)
