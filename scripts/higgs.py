import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the potential for the complex scalar field: V(φ) = μ²|φ|² + λ|φ|⁴
# φ is a complex scalar field, so |φ|² = φ₁² + φ₂²

def higgs_potential(phi1, phi2, mu2, lam):
    return mu2 * (phi1**2 + phi2**2) + lam * (phi1**2 + phi2**2)**2

# Set up grid
phi1 = np.linspace(-2, 2, 200)
phi2 = np.linspace(-2, 2, 200)
phi1, phi2 = np.meshgrid(phi1, phi2)

# Parameters
lam = 2

# Compute potentials for both cases
V_positive_mu2 = higgs_potential(phi1, phi2, mu2=10, lam=lam)
V_negative_mu2 = higgs_potential(phi1, phi2, mu2=-10, lam=lam)

# Plotting
fig = plt.figure(figsize=(14, 6))

# Case 1: mu2 > 0
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(phi1, phi2, V_positive_mu2, cmap='viridis')
ax1.set_title(r'$\mu^2 > 0$')
ax1.set_xlabel(r'$\phi_1$')
ax1.set_ylabel(r'$\phi_2$')
ax1.set_zlabel(r'$V(\phi)$')

# Case 2: mu2 < 0
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(phi1, phi2, V_negative_mu2, cmap='viridis')
ax2.set_title(r'$\mu^2 < 0$')
ax2.set_xlabel(r'$\phi_1$')
ax2.set_ylabel(r'$\phi_2$')
ax2.set_zlabel(r'$V(\phi)$')

plt.tight_layout()
plt.show()
plt.savefig("higgs.png")
