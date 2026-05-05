import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import PyMieScatt as ps


m = 1.5 + 0.01j

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- Left plot: varying wavelength ---
wavelengths = range(375, 800, 25)
# assign colour to each wavelength
colors = cm.plasma(np.linspace(0, 1, len(wavelengths)))
#graph each line of different wavelength on a graph
for wl, color in zip(wavelengths, colors):
    theta, SL, SR, SU = ps.ScatteringFunction(m, wl, diameter=300)
    ax1.semilogy(theta, SU, color=color, label=f"{wl} nm")
ax1.set_xlabel("Angle (degrees)")
ax1.set_ylabel("Scattered intensity (log scale)")
ax1.set_title("Varying wavelength (d = 300 nm)")
ax1.legend(fontsize=6, ncol=2)

# --- Right plot: varying diameter ---
diameters = [2**i for i in range(1, 12)]
# assign colour to each particle with a different diameter
colors = cm.plasma(np.linspace(0, 1, len(diameters)))
# graph each line of particles with different diameters
for d, color in zip(diameters, colors):
    theta, SL, SR, SU = ps.ScatteringFunction(m, wavelength=375, diameter=d)
    ax2.semilogy(theta, SU, color=color, label=f"{d} nm")
ax2.set_xlabel("Angle (degrees)")
ax2.set_ylabel("Scattered intensity (log scale)")
ax2.set_title("Varying diameter (λ = 375 nm)")
ax2.legend(fontsize=6, ncol=2)

plt.tight_layout()
plt.show()

# --- Left plot: varying wavelength ---
# calculate scattering
theta, SL, SR, SU = ps.ScatteringFunction(m, 500, 500)

# mirror the data for degrees 180 - 360
# gets the full cirle
theta_full = np.concatenate([theta, 2*np.pi - theta[::-1]])
SU_full = np.concatenate([SU, SU[::-1]])

# log scale SU values
SU_log = np.log10(SU_full)
SU_log = SU_log - SU_log.min()

# plot in a polar plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta_full, SU_log)
plt.show()

theta, SL, SR, SU = ps.ScatteringFunction(1.5+0.01j, 500, 500)


# print("at 0 degrees:", SU[0])
# print("at 45 degrees:", SU[90])
# print("at 90 degrees:", SU[180])
# print("at 135 degrees:", SU[270])
# print("at 180 degrees:", SU[360])