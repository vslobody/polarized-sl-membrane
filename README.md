# Polarized Sl-Membrane Cosmology

**Status:** conjectural theoretical-physics research program. Timestamped notes are archived on Zenodo. The goal is not to claim a completed theory, but to define a framework that is easy to understand, cite, attack, and test.

## One-sentence claim

Matter/antimatter asymmetry may be branch-relative rather than globally created: a deeper balanced state separates into conjugate branches, while neutral residual stress-energy of the Sl transition may supply a dark relic sector.

## Core idea

The model proposes a three-output early-universe transition:

```text
higher-dimensional balanced state
        ↓ Sl condensation / branch separation
matter-oriented branch A + conjugate branch B + neutral Sl relic residue R_Sl
```

The visible universe is branch A. Global baryon number can remain zero if branch B carries the conjugate orientation. Local Standard Model physics is preserved: positrons, pair creation, annihilation, QED, QCD, and gauge neutrality remain valid inside branch A.

## Current papers

- **Opus I:** `papers/opus_i_polarized_membrane_cosmology.pdf`  
  DOI: `10.5281/zenodo.20991445`  
  Introduces the three-sector membrane yield: branch A, branch B, relic sector R.

- **Opus II:** `papers/opus_ii_polarized_sl_membrane_cosmology.pdf`  
  DOI: `10.5281/zenodo.20991835`  
  Names the Sl membrane and formulates universal orientation sorting.

- **Opus III:** `papers/opus_iii_universal_matter_orientation.pdf`  
  DOI: `10.5281/zenodo.21312037`  
  Treats matter/antimatter orientation as a pre-particle label and clarifies the 40 MeV transition scale.

- **Conjecture I:** `notes/conjecture_i_sl_membrane_relics.pdf`  
  Frames xenon nuclear recoils as a possible future constraint on cold Sl relics, not as evidence.

## What the framework preserves

- Local QED and pair creation: `gamma gamma <-> e+ e-` remains valid.
- Standard Model gauge neutrality inside the observed branch.
- No observable matter/antimatter domains inside our universe.
- Global baryon number may remain zero across conjugate branches.

## What it changes

- The observed matter excess is interpreted as branch-relative selection, not necessarily global baryon creation.
- The matter/antimatter label is treated as deeper than particle species.
- The dark sector is tied to the branch-separation transition rather than introduced independently.

## Main quantitative handles

1. **Matter/photon clock**

   The observed baryon-to-photon ratio estimates the Sl transition epoch:

   ```text
   eta_B ~ 6e-10  ->  T_c ~ 38--40 MeV
   ```

   In this picture, annihilation continues until Sl condensation separates matter-oriented and conjugate-oriented populations.

2. **Relic statistics**

   If the Sl relic sector is dark matter:

   ```text
   m_R n_R ~= 5.3 m_p n_b
   ```

   Define `kappa_R = n_R / n_b`. Then:

   ```text
   m_R ~= (5.3 / kappa_R) m_p
   ```

   The central open problem is deriving `kappa_R`.

3. **First sanity check**

   A naive one-scale scalar condensate with:

   ```text
   m_phi ~ phi_0 ~ T_c ~ 40 MeV
   ```

   overproduces dark matter by roughly `10^6--10^7`. Therefore the relic sector cannot simply inherit every scale from `T_c`.

## Possible observational handles

- Rare nuclear recoils in xenon-type detectors.
- Neutron-star heating or capture constraints.
- Black-hole-adjacent relic instability or enhanced scattering.
- Ultra-high-energy particles from early violent relaxation.
- BBN/CMB and `N_eff` constraints on any radiation-like component.

## Fastest ways to kill the model

- Show the Sl transition cannot preserve branch gauge neutrality.
- Show `T_c ~ 40 MeV` does not follow from annihilation timing.
- Show no viable cold relic sector can satisfy `m_R n_R ~= 5.3 m_p n_b`.
- Show the relic must be radiation-like and therefore violates `N_eff`, BBN, or CMB limits.
- Show any required portal interaction is excluded by direct detection, gas-cloud, accretion-disk, neutron-star, or structure-formation constraints.

## Repository layout

```text
README.md
papers/          archived Opus PDFs
notes/           Conjecture and short technical notes
figures/         overview diagrams and source files
calculations/    toy models and sanity-check scripts
posts/           short public-facing essays
outreach/        ResearchGate/GitHub copy and hostile-review requests
docs/            landing page and one-page summary
references.bib   bibliography seed
CITATION.cff     citation metadata for GitHub
```

## Review request

I am looking for the fastest way to kill this model. The current weak points are relic density, BBN/CMB consistency, defect compactness, recoil conservation, and direct-detection/astrophysical portal constraints. If you see a fatal objection, please point to the shortest calculation or observation that excludes it.
