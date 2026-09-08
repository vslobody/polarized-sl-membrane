"""
Order-of-magnitude relic-statistics sanity check for Conjecture I.

This is not a precision cosmology code. It reproduces the first negative result:
a naive one-scale Sl scalar condensate with m_phi ~ phi_0 ~ T_c ~ 40 MeV
overproduces the observed dark matter density by ~10^6--10^7.
"""

import math

# Inputs
eta_b = 6.0e-10             # baryon-to-photon ratio
s_over_n_gamma = 7.04       # entropy/photon ratio today
omega_dm_over_b = 5.3       # dark-to-baryonic matter density ratio
m_p = 0.938                 # proton mass, GeV
T_c = 0.040                 # Sl transition temperature, GeV = 40 MeV
g_star_s = 14.0             # rough effective entropy degrees of freedom near 40 MeV

# Natural units: entropy density s = (2*pi^2/45) g_*S T^3
s_Tc = (2.0 * math.pi**2 / 45.0) * g_star_s * T_c**3
n_b_over_s = eta_b / s_over_n_gamma
rho_R_over_s_required = omega_dm_over_b * m_p * n_b_over_s
rho_R_Tc_required = rho_R_over_s_required * s_Tc

# Naive one-scale scalar condensate rho = 1/2 m^2 phi0^2, m ~ phi0 ~ T_c
rho_phi_naive = 0.5 * T_c**4
overclosure_factor = rho_phi_naive / rho_R_Tc_required

required_product = math.sqrt(2.0 * rho_R_Tc_required)  # m_phi * phi0 in GeV^2
m_if_phi0_Tc = required_product / T_c
same_scale = math.sqrt(required_product)

print("Inputs")
print(f"eta_b = {eta_b:.2e}")
print(f"Omega_DM/Omega_b = {omega_dm_over_b:.2f}")
print(f"T_c = {T_c:.3f} GeV")
print(f"g_*S = {g_star_s:.1f}")
print()

print("Required relic density")
print(f"n_b/s = {n_b_over_s:.3e}")
print(f"rho_R/s required = {rho_R_over_s_required:.3e} GeV")
print(f"s(T_c) = {s_Tc:.3e} GeV^3")
print(f"rho_R(T_c) required = {rho_R_Tc_required:.3e} GeV^4")
print()

print("Naive one-scale condensate")
print(f"rho_phi naive = 0.5*T_c^4 = {rho_phi_naive:.3e} GeV^4")
print(f"overclosure factor = {overclosure_factor:.3e}")
print()

print("Required scalar product")
print(f"m_phi * phi0 required = {required_product:.3e} GeV^2")
print(f"if phi0 = T_c, m_phi = {m_if_phi0_Tc:.3e} GeV = {m_if_phi0_Tc*1e6:.1f} keV")
print(f"if m_phi = phi0, both = {same_scale:.3e} GeV = {same_scale*1e3:.2f} MeV")
