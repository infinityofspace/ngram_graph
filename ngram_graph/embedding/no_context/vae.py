import torch
from torch import nn, sigmoid


class Decoder(nn.Module):
    def __init__(self, latent_dim=256, hidden_dim=512, output_dim=1024):
        super(Decoder, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
        )

    def forward(self, x):
        return sigmoid(self.layers(x))


class VariationalEncoder(nn.Module):
    def __init__(self, input_dim=1024, hidden_dim=512, latent_dim=256):
        super(VariationalEncoder, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, latent_dim),
        )

        self.mu = nn.Linear(latent_dim, latent_dim)
        self.loh_var = nn.Linear(latent_dim, latent_dim)

    def forward(self, x):
        x = self.layers(x)
        mu = self.mu(x)
        log_var = self.loh_var(x)
        return mu, log_var


class VariationalAutoencoder(nn.Module):
    def __init__(self, input_dim, hidden_dim=512, latent_dim=256):
        super(VariationalAutoencoder, self).__init__()
        self.encoder = VariationalEncoder(input_dim, hidden_dim, latent_dim)
        self.decoder = Decoder(latent_dim, hidden_dim, input_dim)

    def reparameterize(self, mu, log_var):
        std = torch.exp(0.5 * log_var)
        eps = torch.randn_like(std)
        return mu + eps * std

    def forward(self, x):
        mu, log_var = self.encoder(x)
        z = self.reparameterize(mu, log_var)
        return self.decoder(z), mu, log_var


def vae_loss(recon_x, x, mu, log_var):
    reconstruction_loss = nn.functional.binary_cross_entropy(recon_x, x, reduction="sum")
    kld = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp())
    return reconstruction_loss + kld
