import numpy as np
import tqdm
import matplotlib.pyplot as plt
import torch
import torch.nn as nn


sigma = 3.1
# Can pick sigma to be about 3.5 to match our eariler idea.
b = 1.5


from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties
from matplotlib.path import Path


def sample_letters(letters, n_samples=1024, scale=1.0, spacing=1.5, seed=None):
    """
    Sample uniformly from shapes of given letters, centered and arranged in a row.

    Args:
        letters: list of up to 5 characters
        n_samples: total number of samples to draw (split across letters)
        scale: overall scaling of each glyph (applies after normalization)
        spacing: horizontal spacing multiplier between letters (in units of scale)
        seed: random seed
    Returns:
        samples: (n_samples, 2) array of sampled points
        labels: (n_samples,) array of letter indices (which letter each point belongs to)
    """
    if len(letters) == 0:
        return np.empty((0, 2)), np.empty((0,), dtype=int)
    if len(letters) > 5:
        raise ValueError("Can accept up to 5 letters.")

    rng = np.random.default_rng(seed)
    font = FontProperties(family="DejaVu Sans", weight="bold")

    n_letters = len(letters)
    base = n_samples // n_letters
    remainder = n_samples % n_letters
    counts = [base + (1 if i < remainder else 0) for i in range(n_letters)]

    samples_list = []
    labels_list = []

    # Precompute a centered x-offset multiplier so final layout centers at x=0
    center_index = (n_letters - 1) / 2.0

    for i, (ch, count) in enumerate(zip(letters, counts)):
        if count == 0:
            continue

        tp = TextPath((0, 0), ch, size=1.0, prop=font)
        polys = tp.to_polygons()
        if len(polys) == 0:
            # fallback: a small dot at origin
            pts = np.zeros((count, 2))
            pts[:, 0] += (i - center_index) * spacing * 2 * scale
            samples_list.append(pts)
            labels_list.append(np.full(count, i, dtype=int))
            continue

        stacked = np.vstack(polys)
        center = stacked.mean(axis=0)
        denom = np.max(np.abs(stacked - center))
        if denom == 0:
            denom = 1.0

        # scale each polygon consistently
        scaled_polys = [(poly - center) / denom * scale for poly in polys]

        # build a combined Path (verts + codes) for containment tests
        verts_parts = []
        codes_parts = []
        for p in scaled_polys:
            m = len(p)
            if m == 0:
                continue
            # ensure last vertex equals first so CLOSEPOLY has a sensible vertex
            p_local = p.copy()
            if m >= 2:
                p_local[-1] = p_local[0]
            # codes: MOVETO, LINETO*(m-1) but set last to CLOSEPOLY
            codes_local = np.full(m, Path.LINETO, dtype=int)
            codes_local[0] = Path.MOVETO
            codes_local[-1] = Path.CLOSEPOLY
            verts_parts.append(p_local)
            codes_parts.append(codes_local)
        if len(verts_parts) == 0:
            # fallback: small dot
            pts = np.zeros((count, 2))
            pts[:, 0] += (i - center_index) * spacing * 2 * scale
            samples_list.append(pts)
            labels_list.append(np.full(count, i, dtype=int))
            continue

        verts = np.vstack(verts_parts)
        codes = np.concatenate(codes_parts)
        path = Path(verts, codes)

        # bounding box for rejection sampling
        min_xy = verts.min(axis=0)
        max_xy = verts.max(axis=0)
        bbox_area = np.prod(max_xy - min_xy)
        if bbox_area == 0:
            # degenerate bounding box; fallback
            pts = np.zeros((count, 2))
            pts[:, 0] += (i - center_index) * spacing * 2 * scale
            samples_list.append(pts)
            labels_list.append(np.full(count, i, dtype=int))
            continue

        chosen = []
        batch = max(2000, count * 10)
        # rejection sampling using vectorized contains_points
        while len(chosen) < count:
            pts = rng.uniform(min_xy, max_xy, size=(batch, 2))
            mask = path.contains_points(pts)
            if mask.any():
                chosen.extend(pts[mask].tolist())
        chosen = np.array(chosen[:count])

        # offset horizontally so letters sit in a row centered on x=0
        x_offset = (i - center_index) * spacing * 2 * scale
        chosen[:, 0] += x_offset

        samples_list.append(chosen)
        labels_list.append(np.full(count, i, dtype=int))

    samples = np.vstack(samples_list)
    labels = np.concatenate(labels_list)
    return samples, labels


# FIXME: All o the letters are filled in.
# Quick test / demonstration
# letters = ["Z"]
# pts, lbls = sample_letters(letters, n_samples=4000, scale=1.0, spacing=1.2, seed=42)
#
# # Plot result
# plt.figure(figsize=(9, 3))
# plt.scatter(pts[:, 0], pts[:, 1])
# plt.gca().set_aspect("equal")
# plt.title("Sampled letters: " + "".join(letters))
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()


# Example usage
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
    random_t = torch.rand(x.shape[0]) * (1 - eps) + eps  # batch of t's
    cov_scalar = (sigma ** (2 * random_t) - torch.exp(-2 * b * random_t)) / (
        2 * (np.log(sigma) + b)
    )
    std = torch.sqrt(cov_scalar)[:, None]  # shape [batch, 1]

    z = torch.randn_like(x)  # standard normal
    X, Y = x[:, 0], x[:, 1]
    mean_X = torch.exp(-b * random_t) * (
        X * torch.cos(2 * np.pi * random_t) - Y * torch.sin(2 * np.pi * random_t)
    )
    mean_Y = torch.exp(-b * random_t) * (
        X * torch.sin(2 * np.pi * random_t) + Y * torch.cos(2 * np.pi * random_t)
    )
    perturbed_x = torch.stack([mean_X, mean_Y], dim=1) + std * z
    score = model(perturbed_x, random_t)
    loss = torch.mean(torch.sum((std * score + z) ** 2))
    return loss


epochs = 10000
lr = 1e-3
model = SquareNet(2, 128)
optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

losses = []
tqdm_epochs = tqdm.trange(epochs)
for epoch in tqdm_epochs:
    optimizer.zero_grad()
    points = torch.Tensor(
        sample_letters("Z", n_samples=1024, scale=3, spacing=1.2, seed=42)[0]
    )
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
    n_points = 3000
    t = torch.ones(n_points)
    # x = (
    #     1
    #     / 2
    #     * torch.Tensor([[np.sqrt(2), -np.sqrt(2)], [np.sqrt(2), np.sqrt(2)]])
    #     @ (torch.Tensor(sample_hollow_square(1000)).T)
    # ).T
    x = (
        torch.randn(n_points, 2)
        * ((sigma ** (2 * t) - np.e ** (-2 * b * t)) / (2 * (np.log(sigma) + b)))[
            :, None
        ]
    )
    t_range = torch.linspace(1, 1e-5, 1000)
    dt = t_range[0] - t_range[1]

    fig, ax = plt.subplots(figsize=(6, 6))
    scat = ax.scatter(x[:, 0].cpu(), x[:, 1].cpu(), s=5, alpha=1.0)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_aspect("equal")
    ax.set_title("Reverse SDE Sampling")

    def update(frame):
        global x
        t_step = t_range[frame]
        t_feed = torch.ones(x.shape[0], device=x.device) * t_step
        g = diff_coeff(t_feed)

        mean_x = (
            x
            + (
                (g**2)[:, None] * model(x, t_feed)
                - (torch.Tensor([[-b, -2 * np.pi], [2 * np.pi, -b]]) @ x.T).T
            )
            * dt
        )
        x = mean_x + torch.sqrt(dt) * g[:, None] * torch.randn_like(x)

        scat.set_offsets(x.cpu().numpy())
        ax.set_title(f"Reverse SDE Sampling — t = {t_step:.4f}")
        return (scat,)

    anim = FuncAnimation(fig, update, frames=len(t_range), interval=30, blit=True)

    anim.save("reverse_sde_5.mp4", fps=90, dpi=150)
